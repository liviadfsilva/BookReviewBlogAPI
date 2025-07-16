from flask import Flask
from config import DevelopmentConfig
from app.controllers import home, all_reviews

API_PREFIX = "/haunted-musings/api"

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    app.register_blueprint(home, url_prefix=f"{API_PREFIX}/home")
    app.register_blueprint(all_reviews, url_prefix=f"{API_PREFIX}/all-reviews")
    
    return app