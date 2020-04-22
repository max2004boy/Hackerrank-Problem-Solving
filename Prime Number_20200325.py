# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:27:27 2020

@author: max20
"""

def checkPrime(n):
    prime_flag = True
    if n<2:
        prime_flag = False
    elif n==2:
        prime_flag = True
    elif n%2==0:
        prime_flag = False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n%i==0:
                prime_flag = False
    return prime_flag

number_count = int(input())
for j in range(number_count):
    number_temp = int(input())
    if checkPrime(number_temp):
        print('Prime')
    else:
        print('Not prime')