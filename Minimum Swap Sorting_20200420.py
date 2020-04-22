# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:54:22 2020

@author: max20
"""
import timeit

def minimumSwaps(arr):
    arr_set = set(arr)
    swap_count = 0
    
    for i in range(len(arr)):     
        if arr[i] in arr_set:
            circle_size = 1
            arr_set.remove(arr[i])
            next_temp = arr[arr[i]-1]
            while next_temp!=arr[i]:
                circle_size += 1
                arr_set.remove(next_temp)
                next_temp = arr[next_temp-1]
            swap_count += (circle_size-1)
    
    return swap_count

def minimumSwaps2(arr):                   
    arr_copy = arr.copy()
    swap_count = 0
    i = 0
    while(i < len(arr_copy)-1):
        if arr_copy[i] != i+1:
            tmp = arr_copy[i]
            arr_copy[i], arr_copy[tmp-1] = arr_copy[tmp-1], arr_copy[i]
            swap_count += 1
        else:
            i += 1
    return swap_count

if __name__ == '__main__':
#    n = int(input())
#    arr = list(map(int, input().rstrip().split()))
    n = 10
    arr = [9,10,7,8,5,6,3,4,2,1]
    print(minimumSwaps(arr))
    print(minimumSwaps2(arr))
    print(timeit.timeit(lambda:minimumSwaps(arr), number=1000000))
    print(timeit.timeit(lambda:minimumSwaps2(arr), number=1000000))
   