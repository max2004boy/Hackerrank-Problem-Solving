# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:21:10 2020

@author: max20
"""

def commonChild(s1, s2):
    # initiate 2D list of zeros (not allowed to use numpy)
    common_count = []
    for i in range(len(s1)+1):
        common_count.append([0]*(len(s1)+1))
            
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1]==s2[j-1]:
                common_count[i][j] = common_count[i-1][j-1] + 1
            else:
                common_count[i][j] = max(common_count[i-1][j], common_count[i][j-1])
    
    return common_count[len(s1)][len(s2)]


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print(result)