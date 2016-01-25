import socketserver, webbrowser
from dry import utils
from dry.http.request import RequestHandler

PORT = 8000

utils.execfile( 'app/cfg/routes.py' )

httpd = socketserver.TCPServer(('', PORT), RequestHandler)

webbrowser.open('http://localhost:' + str(PORT))

print('serving at port ' + str(PORT))

httpd.serve_forever()