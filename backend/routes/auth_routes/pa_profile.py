from flask import app, render_template, session, flash, redirect, url_for
from backend.decorator.decorators import login_required
from backend.database.supabase import db

def register_pa_profile(app):
    @app.route('/auth/profile')
    @login_required

    def pa_profile():
        return render_template('auth_pages/pa_profile.html')
    
    @app.route('/auth/signout_request')
    def signout_request():
        token = session.get('access_token')
        
        if token:
            db.auth.sign_out()
        session.clear()
        flash('You have been logged out successfully')
        return redirect(url_for('login'))