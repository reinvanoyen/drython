class Response():

    request_handler = None

    @classmethod
    def set_http_response_code(self, response_code):
        self.request_handler.send_response(response_code)

    @classmethod
    def set_content_type(self, content_type):
        self.request_handler.send_header("Content-type", content_type)

    @classmethod
    def output(self, string):
        self.request_handler.wfile.write(string.encode("utf-8"))