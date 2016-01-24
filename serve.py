import socketserver
from http.server import BaseHTTPRequestHandler
from dry import http
from app.cfg.routes import router

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        req = http.Request(self.path)
        router.route(req)

httpd = socketserver.TCPServer(('', 8003), RequestHandler)

print('serving at port 8003')
httpd.serve_forever()