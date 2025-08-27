#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "web"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

os.makedirs(DIRECTORY, exist_ok=True)

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Web Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            background: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }
        .info {
            background: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .success {
            color: #22c55e;
            font-weight: bold;
        }
        code {
            background: #1e293b;
            color: #94a3b8;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Welcome to Your First Web Server!</h1>
        <p class="success">✓ Your local web server is running successfully!</p>
        
        <div class="info">
            <h2>Server Information</h2>
            <p><strong>Server Type:</strong> Python HTTP Server</p>
            <p><strong>Port:</strong> 8000</p>
            <p><strong>URL:</strong> <a href="http://localhost:8000">http://localhost:8000</a></p>
        </div>
        
        <div class="info">
            <h2>What's Happening?</h2>
            <ol>
                <li>Python is running a simple HTTP server</li>
                <li>The server is listening on port 8000</li>
                <li>When you access this URL, the server sends this HTML file</li>
                <li>Your browser receives and renders the HTML</li>
            </ol>
        </div>
        
        <div class="info">
            <h2>Try These Experiments</h2>
            <ul>
                <li>Open Developer Tools (F12) and check the Network tab</li>
                <li>View the page source (Ctrl+U or Cmd+U)</li>
                <li>Try accessing this page from different browsers</li>
                <li>Check the terminal to see server logs</li>
            </ul>
        </div>
        
        <p><strong>Next Step:</strong> Create your own HTML files in the <code>web</code> directory!</p>
    </div>
</body>
</html>"""

if not os.path.exists(f"{DIRECTORY}/index.html"):
    with open(f"{DIRECTORY}/index.html", "w") as f:
        f.write(index_html)

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"🚀 Server starting at http://localhost:{PORT}")
    print(f"📁 Serving files from '{DIRECTORY}' directory")
    print("⌨️  Press Ctrl+C to stop the server\n")
    print("📊 Server Logs:")
    print("-" * 50)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n" + "-" * 50)
        print("🛑 Server stopped.")
        pass