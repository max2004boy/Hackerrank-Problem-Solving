# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:14:27 2020

@author: max20
"""
# Brutal O(n^2)
def substrCount2(n, s):
    sub_count = 0
    # substring length
    for i in range(1,n+1):
        # substring starting index
        for j in range(n-i+1):
            if i==1:
                sub_count+=1
            elif i%2==0:
                sub_tmp = s[j:(j+i)]
                if len(set(sub_tmp))==1:
                    sub_count+=1
            else:
                sub_tmp = s[j:(j+i)]
                if len(set(sub_tmp[:int((i-1)/2)]+sub_tmp[int((i+1)/2):]))==1:
                    sub_count+=1

    return sub_count

# Advanced O(n)
def substrCount(n, s):
    sub_count = 0
    consecutive_count = 0
    last_char = ''
    for i,j in enumerate(s):
        # individual characters
        consecutive_count += 1
        
        
        if i!=0 and (last_char != j):
            # check for patterns such as xxyxx
            k = 1
            # Note: consecutive_count already added 1 for the current character
            while ((i-k)>=0) and ((i+k)<len(s)) and k<consecutive_count: 
                if s[i-k] == s[i+k] == last_char:
                    sub_count += 1
                    k += 1
                else:
                    break
            
            # reset consecutive_count
            consecutive_count = 1
            
        # add consecutive_count to total count (small trick) 
        # example: for 'aaa' first add 1, then add 2, and then add 3
        sub_count += consecutive_count            
        last_char = j
    return sub_count 

if __name__ == '__main__':
    
    n = int(input())
    s = input()

    result = substrCount(n, s)
    print(result)
