from flask import render_template, abort, current_app
import markdown
import os

def register_index(app):
    @app.route("/")
    @app.route("/home")
    def Home():
        return render_template("landing_pages/index.html")
    
    @app.route("/articles/<instrument>/<category>/<slug>")
    def article(instrument, category, slug):
        project_root = current_app.root_path  # directory containing app.py
        content_dir = os.path.join(project_root, "content")

        md_path = os.path.join(content_dir, instrument, category, f"{slug}.md")

        if not os.path.exists(md_path):
            abort(404)

        with open(md_path, "r", encoding="utf-8") as f:
            md_text = f.read()

        html = markdown.markdown(md_text, extensions=["fenced_code", "tables"])

        return render_template(
            "landing_pages/index.html",
            article_html=html
        )