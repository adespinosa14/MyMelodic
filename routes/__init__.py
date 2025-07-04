from .home import register_home
from .privacy import register_privacy

def register_routes(app):
    register_home(app)
    register_privacy(app)