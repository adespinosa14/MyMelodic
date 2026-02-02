from flask import render_template, abort, current_app
from backend.database.supabase import db
import os

def register_categories(app):

    @app.route("/instrument_family/<family>/<instrument>/<category>")

    def category(family, instrument, category):
        response = db.table('categories').select('*, articles(title), instruments!inner(name), category_types!inner(Name)').eq('category_types.Name', category).eq('instruments.name', instrument).execute()
        articles = response.data

        article_list = []

        for i in articles:
            if i['category_types'] is not None:
                article_list.append(i['articles']['title'])

        return render_template('landing_pages/categories.html', family_name=family, instrument_name=instrument, category_name=category, articles=article_list)
