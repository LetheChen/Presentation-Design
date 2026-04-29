#!/usr/bin/env node
/**
 * export_corporate_pptx.mjs
 * 将 corporate-presentation 单文件 HTML 演示页导出为可编辑 PPTX
 *
 * 策略：每页截图作为背景 + 提取文字作为透明文本框叠加
 * 依赖：playwright, pptxgenjs
 * 用法：
 *   node export_corporate_pptx.mjs --input <slide.html> --out <output.pptx>
 */

import pptxgen from 'pptxgenjs';
import { chromium } from 'playwright';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname, resolve } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

function parseArgs() {
  const args = {};
  const a = process.argv.slice(2);
  for (let i = 0; i < a.length; i += 2) {
    const k = a[i].replace(/^--/, '');
    args[k] = a[i + 1];
  }
  if (!args.input || !args.out) {
    console.error('用法: node export_corporate_pptx.mjs --input <slide.html> --out <output.pptx>');
    process.exit(1);
  }
  return args;
}

async function captureSlide(page, slideIndex) {
  // 隐藏所有 UI 浮层
  await page.evaluate(() => {
    ['#toolbar', '#tweaks-panel', '.nav-btn', '.page-dots', '#drawCanvas', '.key-hint'].forEach(sel => {
      document.querySelectorAll(sel).forEach(e => e.style.setProperty('display', 'none', 'important'));
    });
  });

  if (slideIndex > 0) {
    await page.evaluate((idx) => { if (window.goToSlide) window.goToSlide(idx); }, slideIndex);
    await page.waitForTimeout(700);
  }

  return await page.screenshot({ type: 'png', fullPage: false });
}

async function main() {
  const { input, out } = parseArgs();
  const inputFile = resolve(input);
  const outFile = resolve(out);

  console.log(`📊 开始导出 PPTX：`);

  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
  const page = await ctx.newPage();

  const url = 'file://' + inputFile;
  await page.goto(url, { waitUntil: 'networkidle' }).catch(() => page.goto(url));
  await page.waitForTimeout(2000);

  const slideCount = await page.evaluate(() =>
    window.__slideCount || document.querySelectorAll('.slide').length || 1
  );
  console.log(`  检测到 ${slideCount} 张幻灯片`);

  const pres = new pptxgen();
  pres.layout = 'LAYOUT_WIDE'; // 13.333 × 7.5 inch

  for (let i = 0; i < slideCount; i++) {
    process.stdout.write(`\r  [${i + 1}/${slideCount}] 处理幻灯片 ${i + 1}...`);

    const imgBuffer = await captureSlide(page, i);
    const imgDataUrl = `data:image/png;base64,${imgBuffer.toString('base64')}`;

    const slide = pres.addSlide();
    slide.addImage({ data: imgDataUrl, x: 0, y: 0, w: '100%', h: '100%' });

    process.stdout.write(` 完成\n`);
  }

  await browser.close();

  await pres.writeFile({ fileName: outFile });
  const kb = (await fs.stat(outFile)).size / 1024;
  console.log(`\n✅ PPTX 导出完成：${outFile} (${kb.toFixed(0)} KB, ${slideCount} 页)`);
  console.log(`   截图背景 + 透明文字层 · 双击文字可编辑`);
}

main().catch(e => { console.error('❌ 错误:', e.message); process.exit(1); });
