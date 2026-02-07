from flask import app, render_template

def register_contact_me(app):

    @app.route('/contact_me')

    def contact_me():
        return render_template('landing_pages/contact_me.html')
