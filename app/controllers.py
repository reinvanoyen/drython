from dry.route import NotFound

class Pages():

    @staticmethod
    def index(req):
        print( "index" )

    @staticmethod
    def view(req):
        raise NotFound()

class Blog():

    @staticmethod
    def index(req):
        print( "index" )

    @staticmethod
    def view_post(req):
        print(req.parameters.string('page_slug'))
        print(req.parameters.integer('post_id'))