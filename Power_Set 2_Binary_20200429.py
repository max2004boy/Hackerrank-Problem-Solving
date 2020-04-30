# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:51:16 2020

@author: max20
"""
import timeit

# Time Complexity O(n*2^n)
def power_set(s=set()):
    set_len = len(s)
    set_list = list(s)
    power_set_all = set()
    
    # Use binary indicator
    for i in range(2**set_len):
        power_set_tmp = set()
        for j in range(set_len):
            # Check whether jth bit is 1
            if (i & (1 << j) > 0):
                power_set_tmp.add(set_list[j])
        power_set_all.add(frozenset(power_set_tmp))
    
    return power_set_all



if __name__ == '__main__':
    
    #input_set = set(input().split())
    input_set = {'a','b','c','d','e','f','g','h','i','j','k','l'}
    #print(power_set(input_set))
    print(timeit.timeit(lambda: power_set(input_set), number=100))
    