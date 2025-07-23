from app import create_app
from app.seeds.seed_tags import seed_tags

app = create_app()

with app.app_context():
    seed_tags()