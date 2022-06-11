import http.server
import socketserver
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
class Server(BaseHTTPRequestHandler):
    message = "OK"
    def do_GET(self):
        self.send_response(200, message=self.message)
    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        self.message = data["status"]
        self.send_response(201, message=self.message)

def run(server_class=HTTPServer, handler_class=Server, port=8080):
    server_address = ('/api/v1/', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
if __name__ == '__main__':
    run()