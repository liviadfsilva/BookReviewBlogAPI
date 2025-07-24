from app import create_app
from app.seeds.tags import seed_tags

app = create_app()

with app.app_context():
    seed_tags()