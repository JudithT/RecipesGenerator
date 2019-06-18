import unittest
from flask import Flask
from flask import render_template
from server import app

def create_app():
    return app

class FlaskClientTestCase(unittest.TestCase):

        def setUp(self):
                self.app = create_app()
                # self.app_context = self.app.app_context()
                # self.app_csontext.push()
                self.client = self.app.test_client()

        def test_index_page(self):
                response = self.client.get('/')
                self.assertTrue('Delicious Foods' in response.get_data(as_text=True))
                self.assertTrue('Sign Up' in response.get_data(as_text=True))
                self.assertTrue('Sign In' in response.get_data(as_text=True))
        def test_signin_page(self):
                response = self.client.get('/signin')
                self.assertTrue('Email address' in response.get_data(as_text=True))
                self.assertTrue('Password' in response.get_data(as_text=True))
                self.assertTrue('Submit' in response.get_data(as_text=True))

        def test_register_page(self):
                response = self.client.get('/register')
                self.assertTrue('First Name' in response.get_data(as_text=True))
                self.assertTrue('Last Name' in response.get_data(as_text=True))
                self.assertTrue('Email address' in response.get_data(as_text=True))
                self.assertTrue('Password' in response.get_data(as_text=True))
                self.assertTrue('Submit' in response.get_data(as_text=True))

        # def test_homepage_page(self):
        #         response = self.client.get('/homepage')
        #         self.assertTrue('Submit' in response.get_data(as_text=True))

        # def test_recipes_page(self):
        #         response = self.client.get('/recipes')
        #         # self.assertTrue('instructions' in response.get_data(as_text=True))
        #         self.assertTrue('Ingredients' in response.get_data(as_text=True))







        
        
        
        # def test_local_page(self):
        #         response = self.client.get('/signin')
        #         self.assertFalse('Plymouth' in response.get_data(as_text=True))


suite = unittest.TestLoader().loadTestsFromTestCase(FlaskClientTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)