# 🏢 Presentation Design

将文本内容快速转换为专业的企业汇报风格 HTML 演示页，支持画笔标注、配色切换、全屏演示。

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 📊 **HTML 演示** | 浏览器打开即可演示，`← →` 翻页 |
| ✏️ **画笔标注** | 按 `Esc` 调出工具栏，支持画笔/直线/矩形/多颜色 |
| 🎨 **5 套配色** | 企业蓝 / 极简青 / 暖金雅 / 深空黑 / 墨绿稳，实时切换 |
| 📏 **3 档字号** | 紧凑 / 标准 / 宽松，实时切换 |
| ⛶ **全屏演示** | 按 `F` 或点击按钮进入全屏 |
| 📄 **PDF 导出** | 通过 export_server.py 服务器导出（Playwright 渲染） |
| 📊 **PPTX 导出** | 通过 export_server.py 服务器导出（截图背景 + 透明文字层，可直接编辑） |

---

## 🚀 立即使用

1. **生成 HTML**：告诉 OpenClaw「用 Presentation Design skill 生成演示页」
2. **双击打开**：用浏览器（Chrome / Edge 推荐）打开 HTML 文件
3. **启动导出服务器**（如需导出文件）：
   ```bash
   python export_server.py "<HTML文件路径>"
   ```
   服务器启动后会自动打开浏览器，访问地址 `http://localhost:8765/...`

---

## 📁 目录结构

```
Presentation-Design/
├── SKILL.md                    # OpenClaw skill 定义文件
├── template.html               # HTML 演示模板（含全部样式和交互）
├── export_corporate_pdf.mjs  # PDF 导出脚本（可选，手动用）
├── export_corporate_pptx.mjs  # PPTX 导出脚本（可选，手动用）
├── export-helper.py           # 导出辅助脚本（可选）
├── package.json               # 依赖配置（可选，手动用）
└── README.md                  # 本文件
```

---

## 🔧 高级用法（可选）

如果需要更高质量的 PDF 导出（或无网络环境），可以安装依赖后手动导出：

```bash
# 安装依赖
cd ~/.openclaw/skills/Presentation-Design
npm install

# 手动 PDF 导出
node export_corporate_pdf.mjs --input "演示.html" --out "输出.pdf"

# 手动 PPTX 导出
node export_corporate_pptx.mjs --input "演示.html" --out "输出.pptx"
```

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
