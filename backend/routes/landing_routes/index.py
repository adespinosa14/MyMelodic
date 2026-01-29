from flask import render_template, abort, current_app
import markdown
import os

def register_index(app):
    @app.route("/")
    @app.route("/home")
    def Home():
        return render_template("landing_pages/index.html")