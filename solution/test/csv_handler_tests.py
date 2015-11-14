import unittest
import sys

sys.path.append('..')
import csv_handler
import logger


class CsvHandlerTestCase(unittest.TestCase):

    def setUp(self):
        super(CsvHandlerTestCase, self).setUp()
        self.main_logger = logger.init_logger('main')

    def test_incorrect_file_path(self):
        try:
            self.test_csv_handler = csv_handler.CsvHandler(
                '../assets', 'RANDOM.csv', self.main_logger)
            self.assertEqual(True, False) # if we reach here test failed
        except IOError, e:
            self.assertEqual(
                "No csv file with currency exchange rates provided.", e.message
            )
        except Exception, e:
            self.assertEqual(True, False) # if we reach here test failed, another exception thrown

    def test_correct_rates_file_path(self):
        try:
            self.test_csv_handler = csv_handler.CsvHandler(
                '../assets', 'rates.csv', self.main_logger)
        except Exception, e:
            self.assertEqual(True, False) # no exception should be thrown