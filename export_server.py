#!/usr/bin/env python3
"""
export_server.py
企业汇报演示导出服务器

启动后：
- 自动打开浏览器访问 HTML
- 提供 /export/pdf 和 /export/pptx 接口
- 浏览器点击"导出"按钮 → 服务器执行脚本 → 返回下载文件

用法：
  python export_server.py <slide.html>
  python export_server.py <slide.html> --port 8765
  python export_server.py <slide.html> --browser edge   # 指定浏览器
  python export_server.py <slide.html> --no-open       # 不自动打开浏览器
"""

import http.server
import socketserver
import urllib.parse
import os
import sys
import json
import subprocess
import webbrowser
import argparse
import threading
import shutil
from pathlib import Path
from functools import partial

PORT = 8765
HTML_FILE = None
BROWSER = 'edge'
SERVE_DIR = None

# ─────────────────────────────────────────────────────────
# 静态文件服务（给 HTML 用）
# ─────────────────────────────────────────────────────────
class QuietHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        self._directory = directory
        super().__init__(*args, directory=directory, **kwargs)

    def log_message(self, format, *args):
        # 抑制日志，保持干净
        pass

    def do_POST(self):
        # ── 导出接口 ──
        if self.path.startswith('/export/'):
            format = self.path.split('/')[-1]  # 'pdf' 或 'pptx'
            self._handle_export(format)
            return

        self.send_error(404)

    def _handle_export(self, fmt):
        """执行导出脚本，返回文件下载"""
        script_dir = Path(__file__).parent.resolve()
        input_path = Path(HTML_FILE).resolve()

        # 构造输出路径（在临时目录，避免冲突）
        output_name = input_path.stem + f'_导出.{fmt}'
        output_dir = input_path.parent.resolve()
        output_path = output_dir / output_name

        # 找到导出脚本
        script_map = {
            'pdf':  script_dir / 'export_corporate_pdf.mjs',
            'pptx': script_dir / 'export_corporate_pptx.mjs',
        }
        script = script_map.get(fmt)
        if not script or not script.exists():
            self._send_json({'error': f'导出脚本不存在: {script}'}, status=500)
            return

        # 判断 node 路径
        node = shutil.which('node') or 'node'

        cmd = [
            node, str(script),
            '--input', str(input_path),
            '--out',   str(output_path),
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120,
                cwd=str(script_dir),
            )
        except subprocess.TimeoutExpired:
            self._send_json({'error': '导出超时（120秒）'}, status=500)
            return
        except FileNotFoundError:
            self._send_json({'error': '未找到 node，请先安装 Node.js'}, status=500)
            return

        if result.returncode != 0:
            self._send_json({'error': result.stderr or '导出失败'}, status=500)
            return

        if not output_path.exists():
            self._send_json({'error': '输出文件未生成'}, status=500)
            return

        # 返回文件下载
        mime_map = {'pdf': 'application/pdf', 'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'}
        mime = mime_map.get(fmt, 'application/octet-stream')

        with open(output_path, 'rb') as f:
            data = f.read()

        output_path.unlink(missing_ok=True)  # 清理临时文件

        self.send_response(200)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Disposition', f'attachment; filename*=UTF-8\'\'{urllib.parse.quote(output_name)}')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def open_browser(url):
    if BROWSER == 'edge':
        try:
            subprocess.run(
                ['cmd', '/c', 'start', 'microsoft-edge:' + url],
                capture_output=True, timeout=10,
            )
        except Exception:
            webbrowser.open(url)
    elif BROWSER == 'chrome':
        try:
            chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            if os.path.exists(chrome):
                subprocess.Popen([chrome, '--new-window', url])
            else:
                webbrowser.open(url)
        except Exception:
            webbrowser.open(url)
    else:
        webbrowser.open(url)


def main():
    global PORT, HTML_FILE, BROWSER

    parser = argparse.ArgumentParser(description='企业汇报演示导出服务器')
    parser.add_argument('html_file', help='要导出的 HTML 演示文件路径')
    parser.add_argument('--port', type=int, default=8765, help='服务端口（默认 8765）')
    parser.add_argument('--browser', default='edge', choices=['edge', 'chrome', 'none'], help='启动后打开浏览器（默认 edge）')
    parser.add_argument('--no-open', action='store_true', help='不自动打开浏览器')
    args = parser.parse_args()

    HTML_FILE = os.path.abspath(args.html_file)
    PORT = args.port
    BROWSER = args.browser

    if not os.path.exists(HTML_FILE):
        print(f'❌ 文件不存在：{HTML_FILE}')
        sys.exit(1)

    SERVE_DIR = os.path.dirname(os.path.abspath(HTML_FILE))
    os.chdir(SERVE_DIR)

    html_url = f'http://localhost:{PORT}/{os.path.basename(HTML_FILE)}'

    print(f'🚀 服务器启动中...')
    print(f'   端口：{PORT}')
    print(f'   文件：{HTML_FILE}')
    print(f'   导出脚本目录：{os.path.dirname(os.path.abspath(__file__))}')
    print()
    print(f'   访问地址：{html_url}')

    # 自动打开浏览器
    if not args.no_open:
        def _delayed_open():
            import time; time.sleep(1.5)
            open_browser(html_url)
        threading.Thread(target=_delayed_open, daemon=True).start()

    # 启动服务器
    handler = partial(QuietHTTPHandler, directory=SERVE_DIR)
    with socketserver.TCPServer(('localhost', PORT), handler) as httpd:
        print(f'   按 Ctrl+C 停止服务器')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\n👋 服务器已停止')

if __name__ == '__main__':
    main()
