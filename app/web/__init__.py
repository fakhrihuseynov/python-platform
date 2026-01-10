from flask import Flask
from .routes.home import bp as home_bp
from .routes.learn import bp as learn_bp
from .routes.practice import bp as practice_bp
from .routes.flashcards import bp as flashcards_bp
from .routes.coach import bp as coach_bp

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.register_blueprint(home_bp)
    app.register_blueprint(learn_bp, url_prefix="/learn")
    app.register_blueprint(practice_bp, url_prefix="/practice")
    app.register_blueprint(flashcards_bp, url_prefix="/flashcards")
    app.register_blueprint(coach_bp, url_prefix="/coach")
    return app
