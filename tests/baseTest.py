# -*- coding: utf-8 -*-
from flask.ext.testing import TestCase
from flask import Flask
from myfirstflask.app import app, db


class BaseTest(TestCase):

    def create_app(self):
        self.app = Flask(__name__, instance_relative_config=True)
        return self.app

    def setUp(self):
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myfirstflask_test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
