# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 23:02:45 2020

@author: max20
"""

def kaprekarNumbers(p, q):
    num_list = []
    for i in range(p, q+1):
        if i == 1:
            num_list.append(i)
        elif i < 4:    
            continue
        else:
            str_temp = str(i**2)
            # split the squared number into two parts then add them up
            if int(str_temp[-len(str(i)):]) + int(str_temp[:-len(str(i))]) == i:
                num_list.append(i)
    
    if num_list == []:
        print('INVALID RANGE')
    else:
        print(' '.join(map(str, num_list)))

if __name__ == '__main__':
    
    p = int(input())
    q = int(input())

    kaprekarNumbers(p, q)