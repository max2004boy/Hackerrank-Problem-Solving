# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:42:06 2020

@author: max20
"""

def pageCount(n, p):
    # n is number of total pages, p is the page to go to
    return min(p//2, n//2-p//2)
    
if __name__ == '__main__':

    n = int(input())
    p = int(input())

    print(pageCount(n, p))