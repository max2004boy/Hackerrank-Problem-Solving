# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:18:16 2020

@author: max20
"""

# function that calculates the number of games a gamer can buy with
# initial price (p), discount after each game (d), minimum price (m), and budget (s)
def howManyGames(p, d, m, s):
    
    num_game = 0
    while s >= p:
        if p == m:
            # if price has reached the minimum, we can directly calculate the 
            # remaining number of games he can buy
            num_game += (s // m)
            break
        else:
            num_game += 1
            s -= p
            # update price after each item
            p = max(m, p - d)
            
    return num_game

if __name__ == '__main__':
    
    p, d, m, s = map(int, input().split())
    print('Total number of games he can buy is:', howManyGames(p, d, m, s))