from flask import Flask
from initial_routes import register_routes

app = Flask(__name__)
register_routes(app)
