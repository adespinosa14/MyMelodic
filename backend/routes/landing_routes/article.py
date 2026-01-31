from flask import render_template, abort, current_app
import markdown
import os

def register_article(app):
    @app.route("/instrument_family/<family>/<instrument>/<category>/<article>")

    def article(family, instrument, category, article):
        directory = os.path.join('content', family, instrument, category, article)

        if not os.path.exists(directory):
            abort(404)

        html = convert_to_html(directory)

        return render_template('landing_pages/article.html', family_name=family, instrument_name=instrument, category_name=category, article_name=article.replace("_", " ").replace(".md", ""), article=html)
    
# Helper

def convert_to_html(directory):
    with open(directory, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    html = markdown.markdown(md_text, extensions=['fenced_code', 'tables'])

    return html