# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:27:51 2020

@author: max20
"""

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')