#!/bin/env python

import os
import csv

class CsvHandler(object):

	def __init__(self, file_path, file_name, logger):
		"""
		Assumes a two-column csv file. Additional columns will be truncated.
		"""
		self.logger = logger
		self.csv_data = None
		try:
			# assumes a two-column csv file
			with open(os.path.join(file_path, file_name), mode='r') as infile:
				reader = csv.reader(infile)
				next(reader, None)  # skip the headers
				self.csv_data = dict((rows[0],rows[1]) for rows in reader)

			self.logger.info(
				"Data successfully loaded from csv file: %s"
				% os.path.join(file_path, file_name)
			)

		except IOError, e:
			self.logger.error(
				"Couldn't load data from the passed csv file: %s"
				% os.path.join(file_path, file_name)
			)
			# no point running without these values.
			raise IOError('No currency exchange rates provided.')

	def get_csv_data(self):
		return self.csv_data