from flask import render_template, abort
import markdown
from backend.database.supabase import db

def register_article(app):

    @app.route("/instrument_family/<family>/<instrument>/<category>/<article>")
    def article(family, instrument, category, article):
        slug = f'/instrument_family/{family}/{instrument}/{category}/{article.replace(" ", "_")}'

        try:
            response = db.table('articles').select('*').eq('slug', slug).execute()
        except Exception:
            abort(500)

        if not response.data:
            abort(404)

        html = markdown.markdown(response.data[0]['content'])

        return render_template('landing_pages/article.html',
                               family_name=family,
                               instrument_name=instrument,
                               category_name=category,
                               article_name=article,
                               article=html)