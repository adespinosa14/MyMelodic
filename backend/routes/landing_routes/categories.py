from flask import render_template, abort
from backend.database.supabase import db

def register_categories(app):

    @app.route("/instrument_family/<family>/<instrument>/<category>")
    def category(family, instrument, category):
        try:
            response = db.table('categories').select('*, articles(title, summary), instruments!inner(name), category_types!inner(Name)').eq('category_types.Name', category).eq('instruments.name', instrument).execute()
        except Exception:
            abort(500)

        article_list = [i['articles'] for i in response.data if i['category_types'] is not None]

        return render_template('landing_pages/categories.html',
                               family_name=family,
                               instrument_name=instrument,
                               category_name=category,
                               articles=article_list)
