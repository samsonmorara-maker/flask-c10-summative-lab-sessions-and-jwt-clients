from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, migrate, bcrypt, jwt

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
jwt.init_app(app)

import models
from routes import *


if __name__ == "__main__":
    app.run(debug=True)