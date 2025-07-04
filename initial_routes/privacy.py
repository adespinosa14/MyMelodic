from flask import app, render_template

def register_privacy(app):
    @app.route("/privacy")
    def Privacy():
        return render_template('Initial_Home/privacy.html')