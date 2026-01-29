from flask import render_template, abort, current_app
import os

def register_instrument_family(app):
    
    @app.route("/instrument_family/<family>")
    def instrument_family(family):
        family_name = os.path.join(current_app.root_path, 'content', family)

        if not os.path.exists(family_name):
            abort(404)
        
        instruments = []
        for instrument in os.listdir(family_name):
            instruments.append(instrument)

        return render_template("landing_pages/instrument_family.html", family_name=family, instrument_list=instruments)