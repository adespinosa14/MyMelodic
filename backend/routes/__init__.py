from flask import app
from .landing_routes.index import register_index

def register_routes(app):
    register_index(app)