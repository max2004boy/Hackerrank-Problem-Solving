# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:56:33 2020

@author: max20
"""

num_dict = int(input())

phone_dict = {}
for i in range(num_dict):
    phone_temp = input().split()
    phone_dict[phone_temp[0]] = phone_temp[1]

while True:
    try:
        check_num = input()
    except EOFError:
        break
    
    if check_num in phone_dict.keys():
        print(check_num, '=', phone_dict[check_num], sep='')
    else:
        print('Not found')
