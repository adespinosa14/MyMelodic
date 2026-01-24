from flask import Flask, render_template
import os
from backend.routes import register_routes

base_directory = os.path.abspath(os.path.dirname(__file__))
template_directory = os.path.join(base_directory, "frontend", "templates")
static_directory = os.path.join(base_directory, "frontend", "static")

app = Flask(__name__, template_folder=template_directory, static_folder=static_directory)

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)