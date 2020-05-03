# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:43:57 2020

@author: max20
"""

def maxMin(k, arr):
    # first sort the arr from smallest to largest
    arr_sorted = sorted(arr)

    # initialize minimum unfairness variable
    min_unfair = arr_sorted[k-1] - arr_sorted[0]

    # O(n-k) comparison to find the minimum unfairness
    for i in range(1,len(arr_sorted)-k+1):
        if arr_sorted[i+k-1] - arr_sorted[i] < min_unfair:
            min_unfair = arr_sorted[i+k-1] - arr_sorted[i]
            
    return min_unfair


if __name__ == '__main__':

    n = int(input())
    k = int(input())

    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    print('The minimum unfairness between', k, 'elements is:', maxMin(k, arr))