from flask import render_template, abort, current_app
import os
from backend.database.supabase import db

def register_instrument(app):
    
    @app.route("/instrument_family/<family>/<instrument>")

    def instrument(family, instrument):

        instrument = instrument.replace('_', ' ')

        response = db.table('categories').select('category_types(Name), instruments!inner(name)').eq('instruments.name', instrument).execute()
        categories = response.data
        unique_categories = []

        for i in categories:
            if(i['category_types'] not in unique_categories):
                unique_categories.append(i['category_types'])

        print(unique_categories)

        return render_template('landing_pages/instrument.html', 
                               family_name=family, 
                               instrument_name=instrument, 
                               category_list=unique_categories)