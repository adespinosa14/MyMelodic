from flask import render_template, app

def register_login(app):
    @app.route("/login")
    def login():
        return render_template('landing_pages/login.html')

    def login_request():
        print("Login Requested")

    def signup_requested():
        print("Signup Requested")