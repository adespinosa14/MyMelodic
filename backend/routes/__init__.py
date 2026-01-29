from flask import app
from .landing_routes.index import register_index
from .landing_routes.instrument_family import register_instrument_family

def register_routes(app):
    register_index(app)
    register_instrument_family(app)
