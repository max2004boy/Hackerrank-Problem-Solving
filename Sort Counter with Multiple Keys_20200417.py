# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:55:13 2020

@author: max20
"""

from collections import Counter

count_dict = Counter(input())
sorted_keys = sorted(count_dict, key=lambda x:(-count_dict[x],x))

for key in sorted_keys[:3]:
    print(key, count_dict[key])
