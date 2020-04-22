# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:19:59 2020

@author: max20
"""

def wrapper(f):
    def fun(l):
        # complete the function
        f(['+91 {} {}'.format(x[-10:-5],x[-5:]) for x in l])    
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


