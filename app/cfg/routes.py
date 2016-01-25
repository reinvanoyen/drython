from app.controllers.pages import Pages
from dry.route import Router

Router.add( '', [ Pages, 'index' ] )
Router.add( '(?P<page_slug>.+)/', [ Pages, 'view' ] )