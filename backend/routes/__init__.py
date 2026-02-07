from flask import app
from .landing_routes.index import register_index
from .landing_routes.instrument_family import register_instrument_family
from .landing_routes.instrument import register_instrument
from .landing_routes.categories import register_categories
from .landing_routes.article import register_article
from .landing_routes.contact_me import register_contact_me

def register_routes(app):
    register_index(app)
    register_instrument_family(app)
    register_instrument(app)
    register_categories(app)
    register_article(app)
    register_contact_me(app)
