# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:56:30 2020

@author: max20
"""

from itertools import combinations

list_input = input().split()
input_str = list_input[0]
sub_size = int(list_input[1])

sorted_str_list = sorted(list(input_str))
for i in range(sub_size):
    combination_list = list(combinations(sorted_str_list,i+1))
    for item in combination_list:
        print(''.join(map(str,item)))

