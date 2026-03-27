from functools import wraps
from flask import session, redirect, url_for, flash
from backend.database.supabase import db

def login_required(f):
    @wraps(f)
    def function_decorator(*args, **kwargs):
        token = session.get('access_token')

        if not token:
            flash('Please log in to access this page.')
            redirect(url_for('login'))

        try:
            user = db.auth.get_user(token)
            if not user:
                raise Exception('Invalid Token')
        except Exception as e:
            session.clear()
            flash('Your session has expired. Please log in again.')
            return redirect(url_for('login'))
        
        return f(*args, **kwargs)
    return function_decorator