from flask import app, render_template

def register_about(app):
    @app.route("/about")
    def About():
        return render_template("/Initial_Home/about.html")