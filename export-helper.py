#!/usr/bin/env python3
"""
export-helper.py
HTML 内嵌导出助手（无服务器模式）

接收 JSON 参数，通过 Python subprocess 调用 Node.js 导出脚本，
将输出文件 Base64 编码后打印到 stdout，供 JavaScript 捕获下载。

用法（由 HTML 按钮调用）：
  py export-helper.py pdf "<html文件绝对路径>" "<输出文件名.pdf>"
  py export-helper.py pptx "<html文件绝对路径>" "<输出文件名.pptx>"
"""

import sys
import json
import base64
import subprocess
import os
import tempfile
import shutil
from pathlib import Path

SKILL_DIR = Path(__file__).parent.resolve()
SCRIPT_MAP = {
    'pdf':  'export_corporate_pdf.mjs',
    'pptx': 'export_corporate_pptx.mjs',
}

def export_via_node(fmt, html_path, output_name):
    """通过 Node.js subprocess 调用 Playwright 导出"""
    script = SKILL_DIR / SCRIPT_MAP[fmt]
    if not script.exists():
        return None, f"导出脚本不存在: {script}"

    # 在系统 temp 目录生成输出文件
    temp_out = Path(tempfile.gettempdir()) / output_name
    node = shutil.which('node') or 'node'

    cmd = [node, str(script), '--input', str(Path(html_path).resolve()), '--out', str(temp_out)]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120,
            cwd=str(SCRIPT_MAP[fmt]).rsplit('/', 1)[0] if '/' in SCRIPT_MAP[fmt] else '.',
            shell=False,
        )
    except subprocess.TimeoutExpired:
        return None, '导出超时（120秒）'
    except FileNotFoundError:
        return None, '未找到 node，请先安装 Node.js'

    if result.returncode != 0:
        return None, result.stderr or '导出失败'

    if not temp_out.exists():
        return None, '输出文件未生成'

    with open(temp_out, 'rb') as f:
        data = f.read()

    temp_out.unlink(missing_ok=True)
    return base64.b64encode(data).decode('utf-8'), None


def main():
    if len(sys.argv) < 4:
        print(json.dumps({'error': '参数不足，用法：py export-helper.py <pdf|pptx> <html_path> <output_name>'}))
        sys.exit(1)

    fmt = sys.argv[1].lower()
    html_path = sys.argv[2]
    output_name = sys.argv[3]

    if fmt not in SCRIPT_MAP:
        print(json.dumps({'error': f'未知格式：{fmt}，仅支持 pdf/pptx'}))
        sys.exit(1)

    if not os.path.exists(html_path):
        print(json.dumps({'error': f'HTML 文件不存在：{html_path}'}))
        sys.exit(1)

    data, err = export_via_node(fmt, html_path, output_name)
    if err:
        print(json.dumps({'error': err}))
        sys.exit(1)

    print(json.dumps({'data': data, 'name': output_name}))
    sys.exit(0)

if __name__ == '__main__':
    main()
