from flask import render_template, abort, current_app
from backend.database.supabase import db
import os

def register_categories(app):

    @app.route("/instrument_family/<family>/<instrument>/<category>")

    def category(family, instrument, category):

        article_list = []
        response = db.table('categories').select('*, articles(title)').execute()
        articles = response.data

        for article in articles:
            article_list.append(article['articles']['title'])

        return render_template('landing_pages/categories.html', family_name=family, instrument_name=instrument, category_name=category, articles=article_list)
