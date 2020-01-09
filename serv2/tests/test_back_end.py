from serv2 import dice
from flask-testing import TestCase
import pytest
import unittest
import app



class TestBase(TestCase):

    def create_app(self):

        config_name = 'testing'

        return app




class testview(TestBase):


    def test_page_view(self):
        response = self.client.get(url_for('service'))
        self.assertEqual(response.status_code, 200)

    def test_die_100():
        assert type(dice.die_100()) is int
