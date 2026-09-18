import http.server
import socketserver
import webbrowser
import os
import threading

PORT = 8000

os.chdir(r""C:\Users\ks_iv\Downloads\kurikkugame-main\kurikkugame-main\docs"")

# Chromeを指定
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def open_chrome():
    webbrowser.register(
        "chrome",
        None,
        webbrowser.BackgroundBrowser(chrome)
    )
    webbrowser.get("chrome").open(
        f"http://localhost:{PORT}/index.html"
    )

threading.Timer(0.5, open_chrome).start()

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as server:
    print(f"http://localhost:{PORT}/index.html")
    server.serve_forever()