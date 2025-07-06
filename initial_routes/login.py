from flask import app, render_template, request, redirect, jsonify

def register_login(app):
    @app.route('/login')
    def Login():
        return render_template('Initial_Home/login.html')

    @app.route('/login/authenticate_user', methods=['GET', 'POST'])
    def Authenticate_User():
        if request.method == 'POST':
            print(request.form)
        return "<p> Login Successful </p>"