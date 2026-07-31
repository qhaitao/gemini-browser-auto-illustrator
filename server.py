import http.server
import socketserver
import os
import webbrowser

PORT = 8000
DIRECTORY = r"D:\AI\image"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    print(f"🚀 AI 图片画廊服务器正在运行: http://localhost:{PORT}")
    print(f"📁 根目录: {DIRECTORY}")
    print(f"按 Ctrl+C 停止服务器")
    
    # 打开浏览器
    webbrowser.open(f"http://localhost:{PORT}/index.html")

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止。")
