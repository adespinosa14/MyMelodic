from flask import render_template, abort, current_app
import os

def register_instrument(app):
    
    @app.route("/instrument_family/<family>/<instrument>")

    def instrument(family, instrument):

        directory = os.path.join(current_app.root_path, 'content', family, instrument)

        if not os.path.exists(directory):
            abort(404)

        categories = []
        for category in os.listdir(directory):
            categories.append(category)

        return render_template('landing_pages/instrument.html', family_name=family, instrument_name=instrument, category_list=categories)