import unittest
import requests


class UrlTestCase(unittest.TestCase):

    def test_incorrect_url(self):
        response = requests.get('http://127.0.0.1:8888/WRONG_URL')

        self.assertEqual({"status": 404, "msg": "Incorrect request url."}, response.json())
        self.assertEqual(200, response.status_code)

    def test_correct_url(self):
        response = requests.get('http://127.0.0.1:8888/rate/USD/PLN')

        self.assertIn("rate", response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['status'])

class ExchangeRateTestCase(unittest.TestCase):

    def test_incorrect_currency_a(self):
        response = requests.get('http://127.0.0.1:8888/rate/INCORRECT/PLN')

        self.assertEqual({"status": 500, "msg": "Currency INCORRECT not supported."}, response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(500, response.json()['status'])

    def test_incorrect_currency_b(self):
        response = requests.get('http://127.0.0.1:8888/rate/PLN/INCORRECT')

        self.assertEqual({"status": 500, "msg": "Currency INCORRECT not supported."}, response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(500, response.json()['status'])

    def test_correct_currency(self):
        response = requests.get('http://127.0.0.1:8888/rate/USD/PLN')

        self.assertIn("rate", response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['status'])
        # USD / PLN rate 3.782185
        self.assertEqual("3.782185", response.json()['rate'])

    def test_smallcase_currency(self):
        response = requests.get('http://127.0.0.1:8888/rate/usd/pln')

        self.assertIn("rate", response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['status'])
        # USD / PLN rate 3.782185
        self.assertEqual("3.782185", response.json()['rate'])