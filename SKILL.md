---
name: Presentation Design
slug: Presentation-Design
description: "企业汇报演示生成器 - 将文本内容转换为专业的HTML演示页，支持画笔标注、配色切换、字号密度调节、全屏演示、PDF/PPTX一键导出。"
triggers:
  - "生成演示页"
  - "做PPT"
  - "做幻灯片"
  - "汇报材料"
  - "投屏"
  - "演示文稿"
  - "生成演示"
  - "做个汇报"
  - "汇报演示"
  - "企业汇报"
  - "导出PDF"
  - "导出PPTX"
metadata:
  {
    "openclaw": {
      "emoji": "📊",
      "requires": {},
      "install": {
        "kind": "runtime",
        "nodes": ["node"],
        "packages": ["playwright", "pdf-lib", "pptxgenjs"],
        "scripts": ["export_corporate_pdf.mjs", "export_corporate_pptx.mjs", "export-helper.py"],
        "installCommand": "npm install && npx playwright install chromium --with-deps"
      }
    }
  }
---

# 企业汇报演示生成器 v2.1

将文本内容快速转换为专业的企业汇报风格HTML演示页，支持多种设计风格、画笔标注、配色切换、全屏演示，以及 **PDF/PPTX 一键导出**。

---

## 🎯 核心理念

**模板固化，内容注入；风格可选，设计专业；一键导出，交付完整。**

- HTML 模板和功能代码完整内置，换主题只换内容，交互功能永远稳定
- 提供 5 套配色方案 + 3 档字号密度，实时切换，立等可取
- 导出需启动 export_server.py（服务器模式），不支持点击即导出
- 完整的设计确认流程：需求 → 方向确认 → v0草稿 → 完整生成 → **自动化验证** → 交付

---

## 📋 完整工作流

```
用户说"做个汇报"/"生成演示页"
       ↓
【Step 1】需求确认 - 批量问清设计上下文（见必问清单）
       ↓
【Step 2】设计方向确认
  ├─ 需求明确 → 进入 Step 3
  └─ 需求模糊 → 启动「设计方向顾问模式」（5流派×20哲学 → 推荐3方向）
       ↓
【Step 3】声明设计系统 - 在 Markdown 里写出选定的配色/字体/布局/风格
       ↓
【Step 4】v0 草稿 - 用 placeholder + 假设构建前2页，show 给用户确认方向
       ↓
【Step 5】完整生成 - 批量填充内容 + Tweaks 调参
       ↓
【Step 6】自动化验证 - Playwright 检查配色切换/全屏按钮/幻灯片加载
       ↓
【Step 7】交付 - 告知使用方式 + 导出功能说明
```

---

## 🔍 Step 1：需求确认（必问清单）

**开工前必须问清的 5 类问题**，一次性列完让用户批量回答：

### A. 设计上下文（最重要）

1. **这是给谁看的汇报？**（领导层/客户/内部团队/对外演讲/培训）
2. **有公司/项目的品牌规范吗？**（Logo / 主色 / 字体 / 现有PPT模板）
3. **有可以参考的现有设计吗？**（截图/品牌指南/竞品PPT）
4. **汇报的核心信息是什么？**（要让人记住哪3件事）

### B. 风格定位

5. **整体调性偏好？**（严肃专业/活力创新/温暖亲切/科技感/简约克制）
6. **有没有倾向的风格方向？**（没有的话我推荐3个供选择）

### C. 内容结构

7. **内容大概有几块？**（1-2块/3-5块/6块以上）
8. **有没有特别要突出的对比/数据、流程？**（我好设计专门的布局）

### D. 交付形式

9. **只要HTML演示，还是要导出PDF/PPTX？**（两个都要也可以）
10. **需要在演示中做标注吗？**（画笔标注功能默认开启）

> **什么时候可以不问**：用户已给了完整内容大纲+明确风格指示 → 直接进入 Step 3

---

## 🎨 Step 2：设计方向顾问模式

**触发条件**：用户说"做个好看的汇报"/"随便弄一个"/"我不知道要什么风格"

### 哲学风格库（5流派 × 20种设计哲学）

| 编号 | 风格名称 | 哲学内核 | 适合场景 | 推荐指数 |
|------|----------|----------|----------|----------|
| **1-1** | **Pentagram商务风** | 字体即语言，网格即思想。极度克制的颜色（黑白+1个品牌色），瑞士网格系统现代演绎 | 董事会/战略汇报/高密度信息 | ★★★ |
| **1-2** | **Müller-Brockmann传承** | 数学精确的网格（8pt基线），绝对对齐，功能主义至上 | 数据汇报/表格对比/流程说明 | ★★★ |
| **1-3** | **Fathom科学叙事** | 每一个像素都必须承载信息。科学期刊严谨+设计优雅，冷静专业色调 | 研发汇报/数据分析/学术报告 | ★★☆ |
| **1-4** | **Build当代极简** | 精致简单比复杂更难。奢侈品级留白（70%+），微妙字重对比 | 高端客户提案/品牌展示/领导汇报 | ★★☆ |
| **1-5** | **Kenya Hara东方空灵** | 设计不是填充，是清空。极致留白（80%+），白色层次，触觉视觉化 | 创意展示/艺术汇报/精品发布 | ★☆☆ |
| **2-1** | **Locomotive滚动叙事** | 滚动不是浏览，是旅程。电影化分镜叙事，丝滑视差，大胆留白 | 产品发布/品牌故事/历程回顾 | ★★☆ |
| **2-2** | **Sagmeister快乐极简** | 美即功能的情感维度。意外色彩爆发，手工感与数字融合，正能量视觉 | 团队展示/年会/活动汇报 | ★★☆ |
| **2-3** | **Takram日式思辨** | 技术是思考的媒介。概念原型的优雅，柔和科技感（圆角、柔和阴影） | 创新汇报/概念展示/内部研讨 | ★★☆ |
| **2-4** | **Active Theory科技诗** | 让技术可见化即让技术可理解。3D粒子系统，实时渲染数据可视化 | AI/科技产品演示/技术发布 | ★☆☆ |
| **3-1** | **信息建筑派** | 数据不是装饰，是建筑材料。信息层级极度清晰，蓝色超链接传统坚守 | 信息密集型汇报/多章节综合报告 | ★★★ |
| **3-2** | **Stamen数据诗学** | 让数据成为可触摸的风景。地图学思维，有机图形，温暖色调 | 市场分析/用户研究/数据故事 | ★★☆ |
| **3-3** | **Irma Boom书籍建筑** | 信息的物理诗学。非线性信息架构，意外颜色组合（粉+红/橙+棕） | 创意书籍/品牌手册/非传统报告 | ★☆☆ |
| **4-1** | **实验先锋派** | 打破规则即创造规则。单一视觉隐喻贯穿，蒙德里安色系，字体即图形 | 创意行业/设计评审/颠覆性提案 | ★☆☆ |
| **4-2** | **Territory FUI虚构** | 未来UI的今日想象。科幻电影屏幕设计，全息投影感，多层数据叠加 | 科技发布会/未来愿景展示 | ★☆☆ |
| **4-3** | **Zach Lieberman代码诗** | 编程即绘画。手绘感算法图形，实时生成艺术，黑白纯粹表达 | 技术社区/极客分享/创意编程 | ★☆☆ |
| **5-1** | **Neo Shen东方光影** | 技术需要人的温度。水墨晕染数字化，柔和光晕，诗意留白 | 传统文化/中式汇报/东方美学 | ★★☆ |
| **5-2** | **温暖手工感** | 真实触手可及。纸张质感，手工感插画，温暖大地色调 | 社会责任/公益汇报/人文主题 | ★★☆ |

### 推荐流程

当用户需求模糊时，**推荐 3 个来自不同流派的差异化方向**，格式：

```markdown
根据你的汇报场景，我从 5 流派中推荐 **3 个方向**供选择：

**方向A · [流派] · [风格名]**
- 核心理念：[一句话描述]
- 视觉关键词：[3-5个形容词]
- 适合场景：[最适合的汇报类型]

请告诉我倾向哪个方向，或者描述你想要的feel，我来帮你选择。
```

---

## 🎯 Step 3：声明设计系统

**在写第一行 HTML 代码之前**，必须先在 Markdown 里写出设计决策：

```markdown
## 设计决策确认

- **主色系**：#1a365d 深蓝（标题/页眉） + #ed8936 橙色强调
- **辅色系**：#2c5282 中蓝（副标题/对比）
- **背景色**：#f7fafc 浅灰白
- **字体**：Noto Sans SC / PingFang SC / Microsoft YaHei
- **布局**：16:9比例，固定页眉页脚，内容区flex自适应
- **风格**：[选定的哲学风格名]
- **特殊说明**：[如有]
```

---

## 🗂 Step 4：v0 草稿（Junior Designer 模式）

**不要闷头做完整文件**。先做前 2 页草稿，show 给用户确认方向：

### v0 应该包含

- ✅ 封面页（标题/副标题/日期占位）
- ✅ 目录页 或 第一页内容页
- ✅ 标注使用了哪些 placeholder 和 assumptions
- ✅ 列出还没确认的设计决策

### v0 框架示例

```html
<!--
v0 草稿 · 假设确认：

我的假设：
- 受众：领导层，偏好严肃专业风格
- 色调：用企业蓝方案，不需要调
- 内容分3个章节：背景/现状/建议

未确认：
- 副标题内容未知 → 用了 [待用户提供]
- 第3章"建议"部分数据 → 用了 [待提供] 占位
- 是否需要公司logo → [请确认]

方向对了再继续做，谢谢！
-->
```

### v0 交付话术

> v0 草稿已完成（封面 + 目录），方向确认后我会批量生成剩余页面。
>
> **请确认：**
> 1. 配色方案：企业蓝 ✓ / 其他方案？
> 2. 封面标题内容？
> 3. 有没有其他要调整的方向？

---

## 🛠 Step 5：完整生成

### 幻灯片类型速查

| 类型 | 标签 | 用途 |
|------|------|------|
| `slide-cover` | 封面 | 大标题 + 副标题 + 日期，1页 |
| `slide-toc` | 目录 | 章节导航，1页 |
| `slide-content` | 内容页 | 标题 + 正文/列表/卡片/表格，N页 |
| `slide-compare` | 对比页 | 双栏对比，按需 |
| `slide-summary` | 总结页 | 关键要点回顾，1页 |
| `slide-end` | 结束页 | 谢谢观看，1页 |

### 内容布局速查

| 布局 | 适合内容 |
|------|---------|
| `.card` 单栏 | 文字说明、列表 |
| `.two-col` 双栏 | 对比、两类内容 |
| `.three-col` 三栏 | 三要点、三步流程 |
| `.tbl` 表格 | 数据对比、规格对比 |
| `.flow-diagram` 流程图 | 步骤说明、流程展示 |
| `.compare-row` 对比框 | A/B对比、方案对比 |
| `.summary-grid` 总结网格 | 关键要点回顾 |
| `.toc-grid` 目录网格 | 章节导航 |

---

## ✅ Step 6：自动化验证（强制）

**每次交付前必须执行**，使用 Playwright 检查：

### 验证脚本

```javascript
// verify_presentation.cjs
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ channel: 'msedge' });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  await page.goto('file:///path/to/演示.html', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(2000);

  // 1. 配色切换测试
  await page.click('#tweaks-toggle');
  await page.waitForTimeout(200);
  await page.click('[data-action="scheme"][data-value="minimal-cyan"]');
  await page.waitForTimeout(300);
  const color = await page.evaluate(() =>
    getComputedStyle(document.documentElement).getPropertyValue('--primary').trim()
  );

  // 2. 全屏按钮存在
  const fsBtn = await page.evaluate(() => !!document.getElementById('fullscreenBtn'));

  // 3. 幻灯片数量

  // 4. 幻灯片数量
  const slideCount = await page.evaluate(() => document.querySelectorAll('.slide').length);

  await browser.close();
  const pass = errors.length === 0 && color === '#0d5b7a' && fsBtn && slideCount > 0;
  console.log(pass ? '✅ PASS' : '❌ FAIL', '| Errors:', errors.length, '| --primary:', color, '| Slides:', slideCount, '| fullscreenBtn:', fsBtn);
  process.exit(pass ? 0 : 1);
})();
```

**通过标准**：`errors=0` + `--primary=#0d5b7a` + `fsBtn=true` + `slideCount>0`

---

## 📤 Step 7：交付与导出

### 使用方式

1. **浏览器打开** HTML 文件（直接双击即可）
2. **`← →` 翻页**，**`Esc`** 切换标注工具栏，**`F`** 全屏演示
3. **⚙️ 调参**（右下角按钮）：配色方案 / 字号密度 / 显示模式

### 导出功能（需启动导出服务器）

HTML 文件**不含内置导出按钮**。要导出 PPTX/PDF，需手动启动服务器：

```bash
# 进入 skill 目录（OpenClaw 运行时目录）
cd "C:\Users\GS11DZ02279\.openclaw\skills\corporate-presentation"

# 或使用 workspace 备份目录
cd "C:\Users\GS11DZ02279\.openclaw\workspace\skills\Presentation_Design"

# 启动导出服务器（自动打开浏览器）
python export_server.py "<你的HTML文件路径>" [--port 8765] [--browser edge]
```

服务器启动后，在浏览器中点击 ⚙️ 调参 → **PDF** 或 **PPTX** 即可下载。

### 手动导出（可选）

不使用服务器时，也可手动调用脚本：

**PDF 导出：**
```bash
node export_corporate_pdf.mjs --input "演示.html" --out "输出.pdf"
```

**PPTX 导出：**
```bash
node export_corporate_pptx.mjs --input "演示.html" --out "输出.pptx"
```

### 导出效果

| 格式 | 特点 |
|------|------|
| **PDF** | 矢量格式，文字可搜索/复制，背景完整保留 |
| **PPTX** | 截图背景 + 透明文字层，双击文字可直接在 PowerPoint 编辑 |

---

## 📁 关联文件

| 文件 | 说明 |
|------|------|
| `template.html` | HTML 演示模板（含样式和交互，无内置导出按钮） |
| `export_server.py` | 导出服务器（Python HTTP 服务，含 /export/pdf 和 /export/pptx 接口） |
| `export_corporate_pdf.mjs` | PDF 导出脚本（Playwright + pdf-lib） |
| `export_corporate_pptx.mjs` | PPTX 导出脚本（Playwright + pptxgenjs） |
| `export-helper.py` | 导出辅助脚本 |
| `package.json` | 依赖配置 |
| `SKILL.md` | 本文件 |

---

## 🚀 发布到 GitHub（完整流程）

### 1. 初始化 Git 仓库

```bash
cd C:\Users\GS11DZ02279\.openclaw\workspace\skills\Presentation_Design

# 初始化（如果还未初始化）
git init
git add .
git commit -m "feat: Presentation Design v1.0.0
- 企业汇报演示生成器，支持画笔标注/配色切换/全屏
- 内置 PDF 导出（Playwright + pdf-lib）
- 内置 PPTX 导出（Playwright + pptxgenjs）
- export-helper.py 支持 HTML 内嵌直接导出（零服务器）
- 5套配色方案 + 3档字号密度
- 自动化 Playwright 验证"
```

### 2. 创建 GitHub 仓库

在 GitHub 网页上新建仓库，假设命名为 `Presentation-Design`，然后：

```bash
# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/Presentation-Design.git

# 推送
git branch -M main
git push -u origin main
```

### 3. 发布到 ClawdHub（可选）

```bash
# 安装 clawdhub CLI（如果未安装）
npm install -g clawdhub

# 登录
clawdhub login

# 发布
clawdhub publish . --slug Presentation-Design --name "Presentation Design" --version 1.0.0 --changelog "初始版本"
```

### 4. 用户安装（npx 自动安装依赖）

```bash
# 从 GitHub 安装
npx skills add LetheChen/Presentation-Design

# 安装后进入目录安装依赖
cd ~/.openclaw/skills/Presentation-Design
npm install
npx playwright install chromium --with-deps
```

---

## ⚠️ 重要原则

1. **template.html 不可修改**（CSS/JS/HTML 结构是固化资产，生成时只替换内容）
2. **字号规范**：统一用 `clamp(min, preferred, max)`，确保响应式适配
3. **无外部依赖**：最终 HTML 必须是完全自包含的，离线可用
4. **v0 先 show**：不要闷头做完，给用户 course-correct 的机会
5. **占位符诚实**：没内容就用 `[待提供]`，不要编造
6. **配色必须来自设计系统**：禁止在手写颜色时引入新 hex 值
7. **交付前必须验证**：Step 6 自动化脚本 all must pass 才能交付