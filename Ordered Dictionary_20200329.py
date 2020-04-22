# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:40:00 2020

@author: max20
"""

from collections import OrderedDict

sales_book = OrderedDict()
num_item = int(input())

for i in range(num_item):
    input_line = input().split()
    price_temp = int(input_line[-1])
    del input_line[-1]

    if ' '.join(input_line) in sales_book.keys():
        sales_book[' '.join(input_line)] = sales_book[' '.join(input_line)] + price_temp
    else:
        sales_book[' '.join(input_line)] = price_temp

for item in sales_book:
    print(item, sales_book[item])
