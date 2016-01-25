from dry.route import NotFound
from dry.tpl import Template

class Pages():

    @staticmethod
    def index(req):
        tpl = Template()
        tpl.title = 'This is a page index!'
        tpl.render('app/templates/index.tpl')

    @staticmethod
    def view(req):
        tpl = Template()
        tpl.title = 'My page!'
        tpl.render('app/templates/view.tpl')