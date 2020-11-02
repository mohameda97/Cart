import unittest
import json

from flask import Flask
from flaskr import app


class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_total_price(self):
        res = self.client().get('/price/EGP', json={"cart": ["T-shirt", "T-shirt", "Shoes", "Jacket"]})

        self.assertEqual(res.status_code, 200)

    def test_bad_request_cart_empty(self):
        res = self.client().get('/price/USD', json={"cart": []})

        self.assertEqual(res.status_code, 400)

    def test_un_processable_wrong_currency(self):
        res = self.client().get('/price/usd', json={"cart": ["T-shirt", "T-shirt", "Shoes", "Jacket"]})

        self.assertEqual(res.status_code, 422)

    def test_no_cart(self):
        res = self.client().get('/price/USD')

        self.assertEqual(res.status_code, 500)

    def test_get_products(self):
        res = self.client().get('/products')

        self.assertEqual(res.status_code, 200)


    def test_product_not_exist(self):
        res = self.client().get('/price/EGP', json={"cart": ["T-shirt", "T-shirt", "Shoes", "Jacket", "shirt"]})

        self.assertEqual(res.status_code, 400)

    def test_get_offers(self):
        res = self.client().get('/offers')

        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
