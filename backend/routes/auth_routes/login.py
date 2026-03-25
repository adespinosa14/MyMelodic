from flask import render_template, redirect, url_for, request, flash

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
            print(f'{email} -- {password}')
            flash('This is an alart')

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

            print(f'{first_name} {last_name} \n{email}\n{password} - {confirm_password}')
            

        return redirect(url_for('login'))