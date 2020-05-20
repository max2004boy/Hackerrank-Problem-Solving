# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:22:47 2020

@author: max20
"""

def getMoneySpent(keyboards, drives, b):

    min_need = min(keyboards) + min(drives)
    # if b is smaller than the sum of two mins, no need to try other pairs
    if min_need > b:
        return -1
    else:
        final_need = min_need

        for i in keyboards:
            for j in drives:
                if final_need < (i + j) <=b:
                    final_need = i + j
        
        return final_need 


if __name__ == '__main__':
    
    b, n, m = map(int, input().split())

    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    print(getMoneySpent(keyboards, drives, b))