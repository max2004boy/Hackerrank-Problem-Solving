# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 18:18:10 2020

@author: max20
"""

input_list = list(map(int, input().split()))
num_row = input_list[0]
num_col = input_list[1]
num_top_bot = int((num_row-1)/2)
pattern_sample = '.|.'

# Top part
for i in range(num_top_bot):
    pattern_temp = pattern_sample*(2*i+1)
    print(pattern_temp.center(num_col,'-'))

# Middle part
print('WELCOME'.center(num_col,'-'))

# Bottom part
for i in range(num_top_bot):
    pattern_temp = pattern_sample*(2*(num_top_bot-i)-1)
    print(pattern_temp.center(num_col,'-'))