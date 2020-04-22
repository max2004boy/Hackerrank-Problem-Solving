# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:31:47 2020

@author: max20
"""

num_A = int(input())
set_A = set(map(int, input().split()))

num_other = int(input())
for i in range(num_other):
    cmd_temp = input().split()[0]
    eval('set_A.'+cmd_temp+'({})'.format(set(map(int,input().split()))))

print(sum(set_A))