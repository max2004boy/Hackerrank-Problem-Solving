# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 23:20:44 2020

@author: max20
"""

def countingSort(arr):
    # number constraint: 0-99
    arr_counter = [0] * 100

    for i in range(len(arr)):
        # add 1 to the corresponding position when each arr[i] appears
        arr_counter[arr[i]] += 1
    
    return arr_counter

if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print(' '.join(map(str, result)))