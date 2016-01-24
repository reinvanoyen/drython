import re
from dry import utils

class Router():

    def __init__(self):
        self.routes = {}

    def add(self, pattern, controller):
        self.routes[pattern] = controller

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
        print( "ERROR404" )

class NotFound(Exception):
    pass