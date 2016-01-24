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

    def string(self, k):
        return str(self.data.get(k))

    def integer(self, k):
        return int(self.data.get(k))