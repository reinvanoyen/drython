from dry import utils
from dry.http.request import Response

class Template():

    def __setattr__(self, k, v):
        self.__dict__[k]  = v

    def __getattr__(self, k):
        return self.__dict__[k]

    def render(self, filename):

        print( self.__dict__ )

        Response.set_http_response_code(200)
        Response.set_content_type('text/html')

        content = utils.get_file_contents(filename)
        Response.output(content)