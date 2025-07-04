from flask import app, render_template

def register_contact(app):
    @app.route("/contact")
    def Contact():
        return render_template('Initial_Home/contact.html')