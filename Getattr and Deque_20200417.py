# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 21:47:57 2020

@author: max20
"""

from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    cmd_temp, *argument = input().split()
    getattr(d,cmd_temp)(*argument)

print(*d)
