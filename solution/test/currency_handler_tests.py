import unittest
import sys
import os

sys.path.append('..')
import currency_handler
import csv_handler
import logger
import config


class CurrencyHandlerTestCase(unittest.TestCase):

    def setUp(self):
        super(CurrencyHandlerTestCase, self).setUp()

        main_logger = logger.init_logger('main')
        test_csv_handler = csv_handler.CsvHandler(
            os.path.join('..', config.MAIN_CSV_PATH),
            config.RATES_FILE_NAME, main_logger
        )

        self.test_currency_handler = currency_handler.CurrencyHandler(
            test_csv_handler.get_csv_data(), main_logger)

    def test_incorrect_currency(self):
        self.assertEqual(
            False, self.test_currency_handler.is_currency_supported("RANDOM")
        )
        self.assertEqual(
            None, self.test_currency_handler.get_currency_base_exchange_rate("RANDOM")
        )

    def test_incorrect_currency_pair(self):
        self.assertEqual(
            None, self.test_currency_handler.get_currencies_exchange_rate("RANDOM", "USD")
        )
        self.assertEqual(
            None, self.test_currency_handler.get_currencies_exchange_rate("USD", "RANDOM")
        )

    def test_correct_currency_pair(self):
        # https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(
            places = 6, first = 0.2643974,
            second = float(self.test_currency_handler.get_currencies_exchange_rate("PLN", "USD"))
        )
        self.assertAlmostEqual(
            places = 6, first = 3.782185,
            second = float(self.test_currency_handler.get_currencies_exchange_rate("USD", "PLN"))
        )