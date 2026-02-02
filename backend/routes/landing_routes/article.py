from flask import render_template, abort, current_app
import markdown
import os
from backend.database.supabase import db
import json

def register_article(app):
    @app.route("/instrument_family/<family>/<instrument>/<category>/<article>")

    def article(family, instrument, category, article):
        new_article = article.replace(' ', '_')
        url = f'/instrument_family/{family}/{instrument}/{category}/{new_article}'

        response = (db.table('articles').select('*').eq('slug', f'{url}').execute())
        article_content = response.data[0]['content']

        html = convert_to_html(article_content)

        return render_template('landing_pages/article.html', family_name=family, instrument_name=instrument, category_name=category, article_name=article, article=html)
    
# Helper

def convert_to_html(article_content):
    
    html = markdown.markdown(article_content)

    return html