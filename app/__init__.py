from flask import Flask
from config import DevelopmentConfig
from app.controllers import reviews
from app.controllers import auth
from app.controllers import user
from app.controllers import posts
from app.controllers import tags
from flask_migrate import Migrate
from flask_cors import CORS
from app.models.db import db
from app.initializer import jwt
from flask_swagger_ui import get_swaggerui_blueprint

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    CORS(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    app.register_blueprint(reviews, url_prefix="/api/reviews")
    app.register_blueprint(auth, url_prefix="/api")
    app.register_blueprint(user, url_prefix="/api/users")
    app.register_blueprint(posts, url_prefix="/api/blog-posts")
    app.register_blueprint(tags, url_prefix="/api/tags")
    
    SWAGGER_URL = "/docs"
    API_URL = "/static/swagger.json"
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={"app_name": "Book Review Blog API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    return app