# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:35:17 2020

@author: max20
"""

cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fibo = [0,1]
        for i in range(3,n+1):
            num_temp = fibo[-1] + fibo[-2]
            fibo.append(num_temp)
        return fibo

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))