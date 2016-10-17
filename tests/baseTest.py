# -*- coding: utf-8 -*-
from flask.ext.testing import TestCase
from flask import Flask
from giiro.app import app, db
from giiro.models.user import User


class BaseTest(TestCase):

    def create_app(self):
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object('giiro.teste-config')
        app.config.from_pyfile('test-config.cfg', silent=True)
        return app

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        app.config[
            'SQLALCHEMY_DATABASE_URI'] = 'postgresql://giiro:giiro@localhost/testedb'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
