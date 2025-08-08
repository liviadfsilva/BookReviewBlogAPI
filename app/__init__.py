from flask import Flask
from config import DevelopmentConfig
from app.controllers import reviews
from app.controllers import auth
from app.controllers import user
from app.controllers import posts
from flask_migrate import Migrate
from app.models.db import db
from app.initializer import jwt

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    app.register_blueprint(reviews, url_prefix="/api/reviews")
    app.register_blueprint(auth, url_prefix="/api")
    app.register_blueprint(user, url_prefix="/api/users")
    app.register_blueprint(posts, url_prefix="/api/blog-post")
    
    return app