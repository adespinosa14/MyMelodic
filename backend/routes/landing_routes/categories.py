from flask import render_template, abort, current_app
import os

def register_categories(app):

    @app.route("/instrument_family/<family>/<instrument>/<category>")

    def category(family, instrument, category):
        directory = os.path.join(current_app.root_path, 'content', family, instrument, category)

        if not os.path.exists(directory):
            abort(404)
        
        articles = []
        article_names = []
        for article in os.listdir(directory):
            articles.append(article)
            article_names.append(article.replace("_", " ").replace(".md", ""))

        return render_template('landing_pages/categories.html', family_name=family, instrument_name=instrument, category_name=category, article_list=articles, article_name_list=article_names)