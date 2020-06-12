# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:50:16 2020

@author: max20
"""
# StrangeCounter problem 'https://www.hackerrank.com/challenges/strange-code/problem'
# use of for loop and accumulated value
def strangeCounter(t):
    timer_start = 3
    timer_accum = 0
    for i in range(0, 40):
        timer_accum += timer_start * (2 ** i)
        if timer_accum + 1 > t:
            timer_set = timer_accum - timer_start * (2 ** i) + 1
            break
    return timer_start * (2 ** i) - (t - timer_set)

# no need to calulate accumulated value
# use while loop to dynamically deduct the larger and larger timer_start value
def strangeCounter2(t):
    timer_start = 3
    while t > timer_start:
        t -= timer_start
        timer_start *= 2
    return timer_start - t + 1

if __name__ == '__main__':

    t = int(input())

    print(strangeCounter(t))
    print(strangeCounter2(t))