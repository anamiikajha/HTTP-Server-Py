# This server is only meant for development usage and not for the production usage!
from http.server import BaseHTTPRequestHandler, HTTPServer
# server status
print("Server is running on port 8000, use CTRL + C to stop it.")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        page = '''<!doctype html><html class="no-js"lang="en"><head><meta charset="utf-8"><title>Http Server Using Python</title><meta name="description"content=""><meta name="viewport"content="width=device-width,initial-scale=1"><meta property="og:title"content="Http Server"><meta property="og:type"content=""><meta property="og:url"content="http://localhost:8000/"><meta property="og:image"content=""><meta name="theme-color"content="#fafafa"></head><body><h1 style="text-align:center;"class="heading">Python HTTP Server</h1><p style="text-align:center;">This is Simple Http Server</p><div class="dropdown"><p style="margin:0 8px;">This server is only meant for development usage and not for the production usage!</p><ul id="dropmenu"class="list"><li class="dpLists"><a href="https://github.com/anamiikajha/">View Source on Github</a></li></ul></body></html>'''
        self.wfile.write(bytes(page, "utf8"))


with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()
