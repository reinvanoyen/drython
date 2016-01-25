from http.server import BaseHTTPRequestHandler
from dry.http.response import Response
from dry.route import Router

class Request():

    def __init__(self, path):
        self.parameters = RequestDataWrapper()
        self.path = path
        if self.path[0] == '/':
            self.path = self.path[1:]

class RequestDataWrapper():

    def __init__(self, data={}):
        self.data = data

    def set_data(self, data):
        self.data = data

    def str(self, k):
        return str(self.data.get(k))

    def int(self, k):
        return int(self.data.get(k))

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        req = Request(self.path)
        Response.request_handler = self
        Router.route(req)