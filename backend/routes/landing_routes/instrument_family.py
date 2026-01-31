from flask import render_template, abort, current_app
import os
import requests

def register_instrument_family(app):
    
    @app.route("/instrument_family/<family>")
    def instrument_family(family):
        family_name = os.path.join(current_app.root_path, 'content', family)

        if not os.path.exists(family_name):
            abort(404)

        instruments = []

        for instrument in os.listdir(family_name):
            instruments.append(instrument)


        
        instrument_bio = []
        
        for i in instruments:
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{i.lower()}"
            
            request = requests.get(url)
            if request.status_code == 200:
                posts = request.json()

            bio = posts[0]['meanings'][0]['definitions'][0]['definition']
            instrument_bio.append(bio)

        print(instrument_bio)

        return render_template("landing_pages/instrument_family.html", family_name=family, instrument_list=instruments, bio_list=instrument_bio)