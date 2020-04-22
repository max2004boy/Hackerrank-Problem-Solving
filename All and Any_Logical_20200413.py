# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:20:45 2020

@author: max20
"""

n = int(input())
arr = list(map(int, input().split()))
print(all([min(arr)>0, any([str(x)[::-1]==str(x) for x in arr])]))