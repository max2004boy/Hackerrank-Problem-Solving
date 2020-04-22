# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:48:59 2020

@author: max20
"""

import re

n = int(input())
for i in range(n):
    input_str = input()
    try:
        re.compile(input_str)
        print(True)
    except re.error:
        print(False)