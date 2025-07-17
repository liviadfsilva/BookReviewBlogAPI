from flask import Flask
from config import DevelopmentConfig
from app.controllers import reviews

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    app.register_blueprint(reviews, url_prefix="/api/reviews")
    
    return app