import unittest
from flask import url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Effects


class TestBase(TestCase):

    def create_app(self):
 	config_name = 'testing'
        app.config.update(
                SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MY_SQL_USER'))+':'+str(getenv('MY_SQL_PASS'))+'@'+str(getenv('MY_SQL_HOST'))+'/'+str(getenv('MY_SQL_DB_TEST')))
        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        # Create test effect

        effect1 = Effects(id="1", effect="Caster Slapped Hard!")

        effect2 = Effects(id="2", effect="Caster Becomes Invincible for 1 turn")

        db.session.add(effect1)
        db.session.add(effect2)
        db.session.commit()
    
    def tearDown(self):

        db.session.remove()
        db.drop_all()


class testview(Testbase):

    def test_view_page(self):
        response =self.client.get(url_for('data'))
        self.assertEqual(response.status_code, 200)

class test_query_database(TestBase):

    def test_no_of_effects(self):

        self.assertEqual(Effects.query.count(), 2)


