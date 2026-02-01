from flask import render_template, abort, current_app
import os
from backend.database.supabase import db

def register_instrument(app):
    
    @app.route("/instrument_family/<family>/<instrument>")

    def instrument(family, instrument):
        find_categories = db.table('categories').select('*, category_types(Name)').execute()
        the_categories = find_categories.data
        unique_categories = []

        for i in the_categories:
            c_type = i['category_types']['Name']
            if c_type not in unique_categories:
                unique_categories.append(c_type)

        print(unique_categories)

        return render_template('landing_pages/instrument.html', 
                               family_name=family, 
                               instrument_name=instrument, 
                               category_list=unique_categories)