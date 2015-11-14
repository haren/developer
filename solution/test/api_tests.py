import unittest
import requests
import sys

sys.path.append('..')
import config

class UrlTestCase(unittest.TestCase):

    def test_incorrect_url(self):
        response = requests.get('http://127.0.0.1:%s/WRONG_URL' % config.PORT)

        self.assertEqual({"status": 404, "msg": "Incorrect request url."}, response.json())
        self.assertEqual(200, response.status_code)

    def test_correct_url(self):
        response = requests.get('http://127.0.0.1:%s/rate/USD/PLN' % config.PORT)

        self.assertIn("rate", response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['status'])

class ExchangeRateTestCase(unittest.TestCase):

    def test_incorrect_currency_a(self):
        response = requests.get('http://127.0.0.1:%s/rate/INCORRECT/PLN' % config.PORT)

        self.assertEqual({"status": 500, "msg": "Currency INCORRECT not supported."}, response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(500, response.json()['status'])

    def test_incorrect_currency_b(self):
        response = requests.get('http://127.0.0.1:%s/rate/PLN/INCORRECT' % config.PORT)

        self.assertEqual({"status": 500, "msg": "Currency INCORRECT not supported."}, response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(500, response.json()['status'])

    def test_correct_currency(self):
        response = requests.get('http://127.0.0.1:%s/rate/USD/PLN' % config.PORT)

        self.assertIn("rate", response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['status'])
        # USD / PLN rate 3.782185
        self.assertEqual("3.782185", response.json()['rate'])

    def test_smallcase_currency(self):
        response = requests.get('http://127.0.0.1:%s/rate/usd/pln' % config.PORT)

        self.assertIn("rate", response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['status'])
        # USD / PLN rate 3.782185
        self.assertEqual("3.782185", response.json()['rate'])