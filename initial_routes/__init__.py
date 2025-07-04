from .home import register_home
from .privacy import register_privacy
from .about import register_about
from .contact import register_contact
from .login import register_login
from .signup import register_signup

def register_routes(app):
    register_home(app)
    register_privacy(app)
    register_about(app)
    register_contact(app)
    register_login(app)
    register_signup(app)