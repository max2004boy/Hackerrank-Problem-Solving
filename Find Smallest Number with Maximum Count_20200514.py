# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:58:00 2020

@author: max20
"""

def MaximumCount(arr):
    count_dict = {}
    
    # initialize target number with the first element
    # set maximum count to 0
    num_max = arr[0]
    count_max = 0

    for num in arr:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

        if count_dict[num] > count_max:
            count_max = count_dict[num]
            num_max = num
        # if the counts are the equal, set target number to be the smaller one
        elif (count_dict[num] == count_max) and (num < num_max):
            count_max = count_dict[num]
            num_max = num
    
    return num_max

if __name__ == '__main__':
    
    arr = list(map(int, input().rstrip().split()))
    print(MaximumCount(arr))