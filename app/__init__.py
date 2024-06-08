from flask import Flask
from app.database import db, migrate
from app import views


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
    migrate.init_app(app, db)

    app.add_url_rule("/", view_func=views.index_page)

    return app
