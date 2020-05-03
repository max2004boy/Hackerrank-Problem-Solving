# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:34:27 2020

@author: max20
"""

def getMinimumCost(k, c):
    min_cost = 0

    # sort the prices from high to low
    c_sorted = sorted(c, reverse=True)

    for i in range(len(c_sorted)):
        # i//k + 1 as the price multiplier
        min_cost += c_sorted[i] * (i//k + 1)
    
    return min_cost



if __name__ == '__main__':

    n, k = map(int, input().split())
    c = list(map(int, input().rstrip().split()))
    
    print('The minimum cost is:', getMinimumCost(k, c))
