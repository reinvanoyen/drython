import re
from dry import utils
from dry.http.response import Response

class Router():

    routes = {}

    @classmethod
    def add(self, pattern, controller):
        self.routes[pattern] = controller

    @classmethod
    def route(self, req):
        for pattern, controller in self.routes.items():
            search = re.fullmatch(pattern, req.path)
            if search:
                try:
                    req.parameters.set_data( utils.get_named_groups_from_re(pattern, req.path) )
                    controller, method = controller
                    getattr(controller, method)(req)
                    return
                except NotFound:
                    continue

        Response.set_http_response_code(404)
        Response.set_content_type('text/html')
        Response.output('ERROR 404')

class NotFound(Exception):
    pass