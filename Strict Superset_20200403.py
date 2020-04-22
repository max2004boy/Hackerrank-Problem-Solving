# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:03:17 2020

@author: max20
"""

set_A = set(input().split())
set_num = int(input())

superset_ind = True
for i in range(set_num):
    set_temp = set(input().split())
    if (set_temp-set_A)!=set() or (set_A-set_temp)==set():
        superset_ind = False
print(superset_ind)


# Or just use set_A > set_temp