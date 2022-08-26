#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Elements

We'd like you to set up a simple Python library repo on GitHub.
The required bits are: a simple CI via GitHub Actions and a file named `elements.py`.
The `elements` module should provide two functions:

most_common(items: List[str]) which returns the most frequent element from `items

majority(items: List[str]) which returns the majority element (more than 50 % of the list),
or None if there is no majority - using O(n) time and O(1) space, n ~ len(items)

Please consider the resulting library being production grade,
so remember to take care of all the necessities - but don’t overdo it :).
The argument types are illustrative, your code is not required to use typing.
Hand in your solution as a private GitHub repo shared with my GitHub account.
"""

from typing import List
from logni import log

def __cnts(items: List[str]):
	""" sorted(cnts) """

	cnts = {}
	for item in items:
		if item not in cnts:
			cnts[item] = 0
		cnts[item] += 1

	# sort by value
	cnt_sort = sorted(cnts.items(), key=lambda item: item[1], reverse=True)

	return cnts, cnt_sort


def most_common(items: List[str]) -> str:
	""" most_common() - which returns the most frequent element from `items` """
	log.debug('most_common(items=%s)', items)

	# items must be input!
	if not items:
		log.warn('most_common(items=%s) -> ret=None, because items not input',\
			items, priority=3)
		return None

	# sort by values
	cnts, cnt_sort = __cnts(items)
	if not cnt_sort:
		log.warn('most_common(items=%s) -> ret=None, because sorted(%s)=%s',\
			(items, cnts, cnt_sort), priority=3)
		return None

	# return OK
	ret = cnt_sort[0][0]
	log.info('most_common(items=%s) -> ret=%s, because sorted(%s)=%s',\
		(items, ret, cnts, cnt_sort), priority=3)
	return ret


def majority(items: List[str]):
	""" majority() - which returns the majority element
	(more than 50 % of the list), or None if there is no majority -
	using O(n) time and O(1) space, n ~ len(items)
	"""
	log.debug('majority(items=%s)', items)

	# items must be input!
	if not items:
		log.warn('majority(items=%s) -> ret=None, because items not input',\
			items, priority=3)
		return None

	# sort by values
	cnts, cnt_sort = __cnts(items)
	cnt_max = cnt_sort[0][1]
	if not cnt_max:
		log.warn('majority(items=%s) -> ret=None, because cnt_max=%',\
			(items, cnt_max), priority=3)
		return None

	# majority
	rets = []
	cnt_majority = cnt_max / 2
	for item in cnt_sort:
		if item[1] < cnt_majority:
			continue
		rets.append(item[0])

	# return OK
	log.info('majority(items=%s) -> ret=%s, because sorted(%s)=%s',\
		(items, rets, cnts, cnt_sort), priority=3)
	return rets


if __name__ == '__main__':

	log.mask('ALL')
	log.console(True)

	print(most_common(['aa', 'bbb', 'ccc', 'ddd', 'ccc', 'bb', 'eee', 'a', 'ccc', 'ff']))
	print(most_common([]))
	print(most_common(None))
	print()

	print(majority(['aa', 'bbb', 'ccc', 'ddd', 'ccc', 'bb', 'eee', 'aa', 'ccc', 'ff']))
