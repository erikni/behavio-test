#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Element tests
"""

import unittest
from logni import log
from elements import most_common, majority


class UtilTest(unittest.TestCase):
	""" Unit tests """


	def test11_most_ok(self):
		""" most_common() """
		log.debug('--- test11_most_ok() ---')

		items = [\
			['aa',],\
			['aa', 'aa'],\
			['aa', 'aa', 'ccc', 'ddd', 'ccc', 'bb', 'eee', 'a', 'ccc', 'ff'],\
		]

		for item in items:
			ret = most_common(item)
			self.assertIsNotNone(ret)

		print()
		return True


	def test12_most_err(self):
		""" most_common() """
		log.debug('--- test12_most_err() ---')

		items = [(), [], None]
		for item in items:
			ret = most_common(item)
			self.assertIsNone(ret)

		print()
		return True


	def test21_majority_ok(self):
		""" majority() """
		log.debug('--- test21_majority_ok() ---')

		items = [\
			['aa',],\
			['aa', 'aa'],\
			['aa', 'aa', 'ccc', 'ddd', 'ccc', 'bb', 'eee', 'a', 'ccc', 'ff'],\
			['aa', 'bbb', 'ccc', 'ddd', 'ccc', 'bb', 'eee', 'aa', 'ccc', 'ff'],\
		]

		for item in items:
			ret = majority(item)
			self.assertIsNotNone(ret)

		print()
		return True


	def test22_majority_err(self):
		""" majority() """
		log.debug('--- test22_majority_err() ---')

		items = [(), [], None]
		for item in items:
			ret = majority(item)
			self.assertIsNone(ret)

		print()
		return True


if __name__ == '__main__':
	unittest.main()
