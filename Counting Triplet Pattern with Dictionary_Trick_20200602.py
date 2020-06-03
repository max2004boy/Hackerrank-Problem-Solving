# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:08:08 2020

@author: max20
"""

def beautifulTriplets(d, arr):
    # count with a dictionary
    arr_count = {}
    beaut_count = 0
    for i in arr:
        arr_count[i] = arr_count.setdefault(i, 0) + 1
        # since the arr is in ascending order, smaller numbers would be counted first
        # very good trick below
        beaut_count += arr_count.setdefault(i - d, 0) * arr_count.setdefault(i - 2*d, 0)
   
    return beaut_count
            

if __name__ == '__main__':

    n, d = map(int, input().split())
    arr = list(map(int, input().rstrip().split()))

    print("The number of such beautiful triplets is:", beautifulTriplets(d, arr))