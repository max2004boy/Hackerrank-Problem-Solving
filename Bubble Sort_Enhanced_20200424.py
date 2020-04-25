# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:34:09 2020

@author: max20
"""

def countSwaps(a):
    swap_counter = 0
    
    for i in range(1, len(a)):
        temp_counter = 0
        for j in range(len(a)-i):           
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap_counter += 1
                temp_counter += 1
        if temp_counter == 0:
            break

    print('Array is sorted in {} swaps.'.format(swap_counter))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))

if __name__ == '__main__':
    
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)