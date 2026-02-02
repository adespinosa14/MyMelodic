from flask import render_template, abort, current_app
import os
import requests
from backend.database.supabase import db

def register_instrument_family(app):

    ## Main Routing

    @app.route("/instrument_family/<family>")
    def instrument_family(family):
        
        response = db.table('instruments').select('name, description').eq('family', family).execute()
        instrument = response.data

        return render_template("landing_pages/instrument_family.html", 
                               family_name=family, 
                               instrument_list=instrument)
