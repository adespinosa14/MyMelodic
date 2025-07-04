from flask import app, render_template

def register_login(app):
    @app.route('/login')
    def Login():
        return render_template('Initial_Home/login.html')