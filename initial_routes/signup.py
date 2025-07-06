from flask import Flask, app, render_template, request, redirect, jsonify, url_for

def register_signup(app):
    @app.route('/signup')
    def Signup():
        return render_template('Initial_Home/signup.html')

    @app.route('/signup/create_user', methods=['GET', 'POST'])
    def Create_User():
        if request.method == 'POST':
            email_address = request.form['user_email']
            password = request.form['user_password']
            reenter_password = request.form['user_reenter_password']

            print(email_address)
            print(password)
            print(reenter_password)
        
        return "<p> User Created Successfully </p>"
