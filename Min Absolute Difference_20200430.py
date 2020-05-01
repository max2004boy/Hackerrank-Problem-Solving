# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:03:16 2020

@author: max20
"""

def minimumAbsoluteDifference(arr):
    # sort the array first
    arr_sorted = sorted(arr)

    min_diff = arr_sorted[1] - arr_sorted[0]
    for i in range(1, len(arr_sorted)-1):
        if arr_sorted[i+1]-arr_sorted[i] < min_diff:
            min_diff = arr_sorted[i+1]-arr_sorted[i]

    return min_diff


if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(minimumAbsoluteDifference(arr))
