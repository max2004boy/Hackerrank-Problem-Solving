# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:59:49 2020

@author: max20
"""

def luckBalance(k, contests):
    # first sort by luck size
    contests_sorted = sorted(contests, key=lambda x: x[0], reverse=True)
    print()
    luck_sum = 0
    importance_count = 0
    for contest in contests_sorted:
        if contest[1]==0:
            luck_sum += contest[0]
        elif importance_count<k:
            luck_sum += contest[0]
            importance_count += 1
        else:
            luck_sum -= contest[0]
    
    return luck_sum

if __name__ == '__main__':

    n, k = map(int, input().split())
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    print(luckBalance(k, contests))
