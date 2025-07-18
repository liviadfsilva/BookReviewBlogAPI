from flask import Flask
from config import DevelopmentConfig
from app.controllers import reviews
from flask_migrate import Migrate
from app.models.db import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(reviews, url_prefix="/api/reviews")
    
    return app