# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

# App
app = Flask(__name__, instance_relative_config=True)

# Config
app.config.from_object('myfirstflask.config')

# Flask-SQLAlchemy
db = SQLAlchemy(app)

# Automatically create tables
from myfirstflask.models import marker
db.create_all()

# Blueprints
from myfirstflask.routes.app import mod_app
app.register_blueprint(mod_app)

from myfirstflask.routes.marker import mod_marker
app.register_blueprint(mod_marker)

from myfirstflask.routes import errors
