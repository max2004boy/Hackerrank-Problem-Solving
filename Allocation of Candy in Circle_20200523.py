# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:08:33 2020

@author: max20
"""

def candyAllocation(n, m, s):
    candy_loc = s + m -1
    if candy_loc % n == 0:
        return n
    else:
        return candy_loc % n

if __name__ == '__main__':
    
    # number of test cases
    t = int(input())
    
    for t_itr in range(t):
        # n is number of people, m is the number of candies, s is the starting point
        n, m, s = map(int, input().split())
        print('The person to receive the last candy is:', candyAllocation(n, m, s))