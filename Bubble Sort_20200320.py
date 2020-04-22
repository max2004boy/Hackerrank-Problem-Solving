# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:47:32 2020

@author: max20
"""

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap_counter = 0
for i in range(len(a)):
    temp_counter = 0
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            temp_holder = a[j+1]
            a[j+1] = a[j]
            a[j] = temp_holder
            temp_counter+=1
            swap_counter+=1
    if temp_counter==0:
        break

print('Array is sorted in',swap_counter,'swaps.')
print('First Element:',a[0])
print('Last Element:',a[-1])
