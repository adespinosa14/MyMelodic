from flask import render_template, app

def register_login(app):
    @app.route("/login")
    def login():
        return render_template('landing_pages/login.html')