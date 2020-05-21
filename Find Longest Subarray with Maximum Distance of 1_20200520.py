# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:54:28 2020

@author: max20
"""

def pickingNumbers(a):
    # first count the number appearances with a dictionary
    count_dict = {}
    for num in a:
        count_dict[num] = count_dict.setdefault(num, 0) + 1
    
    longest_len = 0
    key_list = sorted(count_dict.keys())
    for i in range(len(key_list)):
        # if not the last number in the sorted dict keys
        if i < len(key_list)-1:
            # add the two consecutive key counts only if they have distance of 1
            if key_list[i+1] - key_list[i] == 1:
                longest_len = max(longest_len, count_dict[key_list[i+1]] + count_dict[key_list[i]])
            else:
                longest_len = max(longest_len, count_dict[key_list[i]])
        else:
            longest_len = max(longest_len, count_dict[key_list[i]])
    
    return longest_len

if __name__ == '__main__':

    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    print(pickingNumbers(a))
