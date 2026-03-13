from flask import render_template, abort
from backend.database.supabase import db

def register_instrument_family(app):

    @app.route("/instrument_family/<family>")
    def instrument_family(family):
        try:
            response = db.table('instruments').select('name, description').eq('family', family).execute()
        except Exception:
            abort(500)

        if not response.data:
            abort(404)

        return render_template("landing_pages/instrument_family.html",
                               family_name=family,
                               instrument_list=response.data)
