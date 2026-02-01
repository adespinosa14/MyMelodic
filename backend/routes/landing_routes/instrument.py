from flask import render_template, abort, current_app
import os
from backend.database.supabase import db

def register_instrument(app):
    
    @app.route("/instrument_family/<family>/<instrument>")

    def instrument(family, instrument):

        directory = os.path.join(current_app.root_path, 'content', family, instrument)

        if not os.path.exists(directory):
            abort(404)

        categories = fill_categories(directory)

        find_instrument_id = (db.table('instruments').select('id').eq("name", instrument).execute())
        instrument_id = find_instrument_id.data[0]['id']
        
        find_categories = db.table('categories').select('*, category_types(Name)').execute()
        the_categories = find_categories.data[0]['category_types']['Name']
        
        

        return render_template('landing_pages/instrument.html', 
                               family_name=family, 
                               instrument_name=instrument, 
                               category_list=categories)
    
## Helper

def fill_categories(directory):
    categories = []
    for category in os.listdir(directory):
        categories.append(category)

    return categories