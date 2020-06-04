# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:23:38 2020

@author: max20
"""

def minimumDistances(a):
    min_d = len(a)
    # use dictionary to record the last observation of each number
    last_dict = {}
    
    # O(n) time complexity
    for i in range(len(a)):
        # O(1)
        if a[i] in last_dict:
            # compare the distance between i and the last observation location
            # with min_d
            min_d = min(min_d, i - last_dict[a[i]])
            last_dict[a[i]] = i
        else:
            # if it is the first observation of the number a[i]
            # add the current location (i) to the dictionary
            last_dict[a[i]] = i

    if min_d == len(a):
        return -1
    else:
        return min_d

if __name__ == '__main__':

    n = int(input())
    a = list(map(int, input().rstrip().split()))

    print('The minimum distance between same numbers is:', minimumDistances(a))