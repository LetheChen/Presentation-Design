# 🏢 Presentation Design

将文本内容快速转换为专业的企业汇报风格 HTML 演示页，支持画笔标注、配色切换、全屏演示，以及 **PDF / PPTX 一键导出**（无需任何服务器，开箱即用）。

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 📊 **HTML 演示** | 浏览器打开即可演示，`← →` 翻页 |
| ✏️ **画笔标注** | 按 `Esc` 调出工具栏，支持画笔/直线/矩形/多颜色 |
| 🎨 **5 套配色** | 企业蓝 / 极简青 / 暖金雅 / 深空黑 / 墨绿稳，实时切换 |
| 📏 **3 档字号** | 紧凑 / 标准 / 宽松，实时切换 |
| ⛶ **全屏演示** | 按 `F` 或点击按钮进入全屏 |
| 📄 **PDF 导出** | 矢量格式，文字可搜索/复制，直接下载 |
| 📊 **PPTX 导出** | 截图背景 + 透明文字层，双击可直接编辑，直接下载 |

---

## 🚀 快速开始

### 首次安装（一次性）

```bash
# 安装 skill
npx skills add LetheChen/Presentation-Design

# 进入目录安装依赖
cd ~/.openclaw/skills/Presentation-Design
npm install
npx playwright install chromium --with-deps
```

> **`npx skills add` 不会自动运行 npm install**，所以需要手动执行上面的 `npm install` 和 `playwright install` 步骤（只需一次）。

### 使用导出功能

1. 用 Presentation Design skill 生成 HTML 演示文件
2. 双击用浏览器打开 HTML 文件
3. 点击右下角 **⚙️ 调参** → **📄 PDF** 或 **📊 PPTX**，直接下载

> 导出功能需要本地安装 **Python 3.8+** 和 **Node.js**（用于调用 Playwright 渲染）。

---

## 📁 目录结构

```
Presentation-Design/
├── SKILL.md                    # OpenClaw skill 定义文件
├── template.html               # HTML 演示模板（含全部样式、交互、导出逻辑）
├── export_corporate_pdf.mjs   # PDF 导出脚本（手动导出用）
├── export_corporate_pptx.mjs   # PPTX 导出脚本（手动导出用）
├── export-helper.py            # 导出辅助脚本（HTML 内嵌调用）
├── package.json                # 依赖配置
└── README.md                   # 本文件
```

---

## 🔧 依赖

| 依赖 | 版本 | 用途 |
|------|------|------|
| `playwright` | ^1.52.0 | 浏览器渲染/截图 |
| `pdf-lib` | ^1.17.1 | PDF 合并生成 |
| `pptxgenjs` | ^3.12.0 | PPTX 生成 |
| `Python 3` | 3.8+ | 启动 Playwright 渲染（必须） |
| `Node.js` | 18+ | 运行导出脚本（必须） |

---

## 🎨 配色方案

| 方案 | 主色 | 适合场景 |
|------|------|----------|
| 企业蓝 | `#1a365d` | 正式汇报、董事会、战略 |
| 极简青 | `#0d5b7a` | 科技感、创新、数据 |
| 暖金雅 | `#78350f` | 高端提案、品牌、精品 |
| 深空黑 | `#0f172a` | 暗场演讲、科技发布 |
| 墨绿稳 | `#14532d` | 稳健汇报、合规、绿能 |

---

## ⌨️ 快捷键

| 快捷键 | 功能 |
|--------|------|
| `← →` | 上一页 / 下一页 |
| `Esc` | 显示/隐藏标注工具栏 |
| `F` | 切换全屏模式 |
| 双击 | 显示/隐藏标注工具栏 |

---

## 📤 手动导出（可选）

不想用 HTML 内嵌导出按钮？也可以手动调用脚本：

```bash
# PDF 导出
node export_corporate_pdf.mjs --input "演示.html" --out "输出.pdf"

# PPTX 导出
node export_corporate_pptx.mjs --input "演示.html" --out "输出.pptx"
```

---

## 🤖 OpenClaw Skill 安装命令

```bash
npx skills add LetheChen/Presentation-Design
```

---

## 📖 设计哲学

本工具基于 **「模板固化，内容注入」** 的理念：

- HTML 模板和功能代码完整内置，换主题只换内容，交互功能永远稳定
- 不同模型、不同话题都输出稳定一致的演示页
- 完整的设计确认流程：需求 → 方向确认 → v0草稿 → 完整生成 → 自动化验证 → 交付

---

*License: MIT · 适合企业汇报、方案展示、技术分享等场景*
