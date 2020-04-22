# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:02:12 2020

@author: max20
"""

size_k = int(input())
room_entries = list(map(int, input().split()))
all_set = set()
all_family_set = set()

for i in range(len(room_entries)):
    if room_entries[i] in all_set:
        all_family_set.add(room_entries[i])
    else:
        all_set.add(room_entries[i])

print(*(all_set-all_family_set))