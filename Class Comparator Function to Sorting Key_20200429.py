# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:51:38 2020

@author: max20
"""

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return (self.name, self.score)
        
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0

if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        name, score = input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)
    
    # Use class comparator function to convert to sorting keys
    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)