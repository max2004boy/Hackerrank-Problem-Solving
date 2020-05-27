# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:40:00 2020

@author: max20
"""

def appendAndDelete(s, t, k):
    # first count the number of minimum append and delete operations needed
    min_op = len(s) + len(t)
    for i in range(min(len(s), len(t))):
        if s[i]==t[i]:
            min_op -= 2
        else:
            break
    # Case 1: k < minimum number of operations, then 'No'
    if k < min_op:
        return 'No'
    # Case 2: k and the minimum number of operations are even or odd at the same time, then 'Yes'
    # could keep appending one character and deleting it immediately
    elif k % 2 == min_op % 2:
        return 'Yes'
    # Case 3: k is larger than the total length of two strings, then 'Yes'
    # could keep deleting (nothing) when string is empty
    elif k > len(s) + len(t):
        return 'Yes'
    # All other cases will return 'No'
    else:
        return 'No'

if __name__ == '__main__':
    
    s = input()
    t = input()
    k = int(input())

    print(appendAndDelete(s, t, k))