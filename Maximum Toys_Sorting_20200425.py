# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:04:59 2020

@author: max20
"""

def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    toy_num = 0
    for i in sorted_prices:
        if k>=i:
            toy_num += 1
            k -= i
        else:
            break
    return toy_num
    

if __name__ == '__main__':

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
