print("hello") 
print("modified test.py")
#print("modifie in remote")
print("added as part of new_feature2")

import unittest
from flask import Flask, jsonify
from flask_testing import TestCase
import uuid
import string
import random
import time
from your_flask_app_file import app  # Replace 'your_flask_app_file' with the name of your Python file

class TestFlaskApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, World!", response.data)

    def test_welcome_route(self):
        response = self.client.get('/welcome')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Flask Tutorials", response.data)

    def test_response_from_llm_route(self):
        response = self.client.get('/response_from_llm')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('uid', data)
        # Check if uid is a valid UUID
        try:
            uuid.UUID(data['uid'])
        except ValueError:
            self.fail("uid is not a valid UUID")

    def test_message_id_route(self):
        response = self.client.get('/message_id')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('uid', data)
        # Check if uid is a valid UUID
        try:
            uuid.UUID(data['uid'])
        except ValueError:
            self.fail("uid is not a valid UUID")

    def test_nonexistent_route(self):
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()