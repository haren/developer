#!/bin/env python

from decimal import Decimal

class CurrencyHandler(object):

	def __init__(self, rates):
		"""
		rates - {'currency_code': exchange_rate}
		"""
		self.rates = {
			k: Decimal(v)
			for k,v in rates.items()
		}

	def is_currency_supported(self, currency_code):
		return currency_code.upper() in self.rates.keys()

	def get_currency_base_exchange_rate(self, currency_code):
		"""
		Returns the base rate between the passed currency and the USD.
		"""
		if not self.is_currency_supported(currency_code):
			return None
		return self.rates[currency_code]

	def get_currencies_exchange_rate(self, currency_a, currency_b):
		a_usd = self.get_currency_base_exchange_rate(currency_a)
		b_usd = self.get_currency_base_exchange_rate(currency_b)

		if not a_usd or not b_usd:
			return None
		return a_usd / b_usd