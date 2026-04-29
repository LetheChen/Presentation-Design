#!/usr/bin/env node
/**
 * export_corporate_pdf.mjs
 * 将 corporate-presentation 单文件 HTML 演示页导出为矢量 PDF
 *
 * 依赖：playwright, pdf-lib
 * 用法：
 *   node export_corporate_pdf.mjs --input <slide.html> --out <output.pdf> [--width 1920] [--height 1080]
 */

import { chromium } from 'playwright';
import { PDFDocument } from 'pdf-lib';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname, resolve } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

function parseArgs() {
  const args = { width: 1920, height: 1080 };
  const a = process.argv.slice(2);
  for (let i = 0; i < a.length; i += 2) {
    const k = a[i].replace(/^--/, '');
    args[k] = a[i + 1];
  }
  if (!args.input || !args.out) {
    console.error('用法: node export_corporate_pdf.mjs --input <slide.html> --out <output.pdf> [--width 1920] [--height 1080]');
    process.exit(1);
  }
  args.width = parseInt(args.width);
  args.height = parseInt(args.height);
  return args;
}

async function main() {
  const { input, out, width, height } = parseArgs();
  const inputFile = resolve(input);
  const outFile = resolve(out);

  console.log(`📄 开始导出 PDF：`);

  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width, height } });
  const page = await ctx.newPage();

  const url = 'file://' + inputFile;
  await page.goto(url, { waitUntil: 'networkidle' }).catch(() => page.goto(url));
  await page.waitForTimeout(2000);

  // 隐藏 UI 浮层
  await page.evaluate(() => {
    ['#toolbar', '#tweaks-panel', '.nav-btn', '.page-dots', '.key-hint', '#drawCanvas'].forEach(sel => {
      document.querySelectorAll(sel).forEach(el => el.style.setProperty('display', 'none', 'important'));
    });
  });

  const slideCount = await page.evaluate(() =>
    window.__slideCount || document.querySelectorAll('.slide').length || 1
  );
  console.log(`  检测到 ${slideCount} 张幻灯片`);

  const pageBuffers = [];

  for (let i = 0; i < slideCount; i++) {
    if (i > 0) {
      await page.evaluate((idx) => { if (window.goToSlide) window.goToSlide(idx); }, i);
      await page.waitForTimeout(600);
    }

    await page.emulateMedia({ media: 'screen' });
    const buf = await page.pdf({
      width: `${width}px`,
      height: `${height}px`,
      printBackground: true,
      margin: { top: 0, right: 0, bottom: 0, left: 0 },
      preferCSSPageSize: false,
    });
    pageBuffers.push(buf);
    process.stdout.write(`\r  [${i + 1}/${slideCount}] 页面 ${i + 1} 完成`);
  }

  await browser.close();
  console.log('');

  // 合并 PDF
  const merged = await PDFDocument.create();
  for (const buf of pageBuffers) {
    const src = await PDFDocument.load(buf);
    const copied = await merged.copyPages(src, src.getPageIndices());
    copied.forEach(p => merged.addPage(p));
  }

  const bytes = await merged.save();
  await fs.writeFile(outFile, bytes);

  const kb = (bytes.byteLength / 1024).toFixed(0);
  console.log(`\n✅ PDF 导出完成：${outFile} (${kb} KB, ${slideCount} 页)`);
  console.log(`   矢量格式 · 文字可搜索 · 背景完整保留`);
}

main().catch(e => { console.error('❌ 错误:', e.message); process.exit(1); });
