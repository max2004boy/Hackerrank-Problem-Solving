# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:36:09 2020

@author: max20
"""

def print_rangoli(size):
    # your code goes here
    alph_list = [chr(ord('a')+i) for i in range(26)]
    rangoli_list = []
    column_num = 4*size-3

    # Top and middle part
    for i in range(size):
        alph_temp = alph_list[(size-i-1):size]
        line_temp = '-'.join(alph_temp[:0:-1] + alph_temp)
        rangoli_list.append(line_temp.center(column_num,'-'))
    
    # Bottom part
    for i in range((size-1)):
        alph_temp = alph_list[(i+1):size]
        line_temp = '-'.join(alph_temp[:0:-1] + alph_temp)
        rangoli_list.append(line_temp.center(column_num,'-'))
    
    print('\n'.join(rangoli_list))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)