# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:20:16 2020

@author: max20
"""

import random
import timeit
import math

def f(arr):
	"""
	O(nlogn + 2n)
	"""
	arr = sorted(arr)
	return (sum(arr[0:4]),sum(arr[1:5]))

def g(arr):
	"""
	O(3n)
	"""
	asum = sum(arr)
	return (asum-(max(arr))), (asum-(min(arr)))

def h(arr):
	"""
	O(n)
	"""
	amin = math.inf
	amax = -math.inf
	asum = 0
	for a in arr:
		if a < amin: amin = a
		if a > amax: amax = a
		asum += a
	return (asum-amax,asum-amin)

random.seed()
arr = list(random.sample(range(10**16),5))

print(timeit.timeit('f(arr)', globals=globals()))
print(timeit.timeit('g(arr)', globals=globals()))
print(timeit.timeit('h(arr)', globals=globals()))
