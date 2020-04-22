# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:41:06 2020

@author: max20
"""

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        
        if k|(k-1)<=n:
            print(k-1)
        else:
            print(k-2)

