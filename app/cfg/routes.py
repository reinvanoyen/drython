from app.controllers import Pages, Blog
from dry.route import Router

router = Router()
router.add( '/', [ Pages, 'index' ] )
router.add( '(?P<page_slug>.+)/', [ Pages, 'view' ] )
router.add( 'blog/', [ Blog, 'index' ] )
router.add( 'blog/(?P<post_id>\d+)/', [ Blog, 'view_post' ] )