from flask import app, render_template
from backend.decorator.decorators import login_required

def register_pa_home(app):
    @app.route("/auth/home")
    @login_required

    def pa_home():
        return render_template('auth_pages/pa_home.html')