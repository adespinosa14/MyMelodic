from flask import app, render_template

def register_signup(app):
    @app.route('/signup')
    def Signup():
        return render_template('Initial_Home/signup.html')
