from flask import render_template, redirect, url_for, request, flash
from backend.database.supabase import db

def register_login(app):
    @app.route("/login")
    def login():
        return render_template('landing_pages/login.html')
    
    @app.route("/login_request", methods=['GET', 'POST'])
    def login_request():
        if request.method == 'POST':
            data = request.form
            email = data['email']
            password = data['password']

            try:
                db.sign_in_with_password({
                    'email' : email,
                    'password' : password
                })

                redirect(url_for(''))
            except Exception as e:
                flash(f'Login Error: {e}')
                return redirect(url_for('login'))

        return redirect(url_for('login'))

    @app.route("/signup_request", methods=['GET', 'POST'])
    def signup_request():
        if request.method == 'POST':
            data = request.form
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            password = data['password']
            confirm_password = data['confirm_password']

            if password != confirm_password:
                flash('Passwords Don\'t Match')
                return redirect(url_for('login'))
            try:
                db.auth.sign_up({
                    'email': email,
                    'password': password,
                    'options': {
                        'data' : {
                            'first_name': first_name,
                            'last_name': last_name
                        },
                        'email_redirect_to': url_for('login', _external=True)
                    }
                })

                flash('Signup Successful - Please Login', 'success')
            except Exception as e:
                flash(f'Signup Error: {e}')
                return redirect(url_for('login'))
            
        return redirect(url_for('login'))