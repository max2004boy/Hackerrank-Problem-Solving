# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:57:26 2020

@author: max20
"""

from itertools import product

k, m = map(int, input().split())
num_arr = [list(map(int,input().split()))[1:] for _ in range(k)]

num_product = list(product(*num_arr))
func_value = [sum(map(lambda x: x**2,i))%m for i in num_product]
print(max(func_value))