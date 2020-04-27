# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:03:16 2020

@author: max20
"""

def stepPerms(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4   
    # only need to calculate once for each n
    # use dictionary
    elif n in stair_dict:
        return stair_dict[n]
    else:
        stair_dict[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
        return stair_dict[n]


if __name__ == '__main__':

    s = int(input())
    stair_dict = dict()

    for s_itr in range(s):
        n = int(input())
        print(stepPerms(n))