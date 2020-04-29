# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:39:01 2020

@author: max20
"""

def sherlockAndAnagrams(s):
    anagram_counter = 0
    
    # establish sorted substring dictionary
    substr_dict = {}
    for sub_len in range(1, len(s)):
        for i in range(len(s)-sub_len+1):
            substr_tmp = ''.join(sorted(s[i:(i+sub_len)]))
            substr_dict[substr_tmp] = substr_dict.setdefault(substr_tmp, 0) + 1
    
    # find number of anagrams
    # combinations ("n choose 2")
    for substr in substr_dict:
        anagram_counter += substr_dict[substr]*(substr_dict[substr]-1)/2
    
    return int(anagram_counter)
    

if __name__ == '__main__':
    
    q = int(input())
    
    for q_itr in range(q):
        s = input()
        print(sherlockAndAnagrams(s))