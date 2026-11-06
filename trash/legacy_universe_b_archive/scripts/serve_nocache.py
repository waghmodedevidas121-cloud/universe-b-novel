import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = r"D:\Web Novel\UNIVERSE B\New"

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Force browser to never cache any file served by this studio server
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    # Allow port reuse immediately
    socketserver.TCPServer.allow_reuse_address = True
    print(f"Starting Zero-Cache HTTP Server on port {PORT} serving {DIRECTORY}...")
    with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            print("Server stopped.")
