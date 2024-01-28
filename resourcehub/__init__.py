import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.config["UPLOAD_FOLDER"] = "resourcehub/static/files"

db = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = "home"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

from resourcehub import routes, models  # noqa
from resourcehub.models import User

