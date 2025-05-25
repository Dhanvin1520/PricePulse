from flask import Flask
from app.database import init_db
from app.scheduler import schedule_scraping

def create_app():
    app = Flask(__name__)
    init_db()
    schedule_scraping()
    from app.routes import bp
    app.register_blueprint(bp)
    return app