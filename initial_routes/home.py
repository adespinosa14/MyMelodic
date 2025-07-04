from flask import app, render_template

def register_home(app):
    @app.route("/")
    @app.route("/home")
    def Home():
        return render_template("Initial_Home/index.html")