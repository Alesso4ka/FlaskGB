import os

from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.auth import login_manager, auth_app
from blog.views.authors import authors_app
from blog.models.database import db
from blog.security import flask_bcrypt
from blog.admin import admin
from blog.api import init_api
from flask_migrate import Migrate

cfg_name = "DevConfig"

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(auth_app, url_prefix="/auth")
    app.register_blueprint(authors_app, url_prefix="/authors")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "abcdefg123456"
    app.config.from_object(f"blog.configs.{cfg_name}")

    flask_bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    init_api(app)


    migrate = Migrate(app, db, compare_type=True)
    return app



@app.route("/")
def index():
    return render_template("index.html")
