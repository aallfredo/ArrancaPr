from pyramid.config import Configurator

try:
    # for python 2
    from urlparse import urlparse
except ImportError:
    # for python 3
    from urllib.parse import urlparse

import pymongo
from pymongo import MongoClient
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('project', '/project')
    config.add_route('contact', '/contact')
    config.scan()

    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = MongoClient(settings['mongo_uri'])

    def get_db(request):
        db = config.registry.db[db_url.path[1:]]
        return db
    config.add_request_method(get_db, 'db', reify=True)
    return config.make_wsgi_app()
