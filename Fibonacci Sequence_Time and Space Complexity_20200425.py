# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:55:54 2020

@author: max20
"""
import timeit

# Recursive
# O(2^n) time complexity, O(n) space complexity
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Iterative
# O(n) time complexity, O(1) space complexity
def fibonacci_2(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else: 
        fibo = [0, 1]
        for i in range(2, n+1):
            fibo[i%2] = fibo[0] + fibo[1]
        return fibo[i%2]
    

if __name__ == '__main__':
    
    n = int(input())
    
    print(fibonacci(n))
    print(timeit.timeit(lambda: fibonacci(n),number=1))
    
    print(fibonacci_2(n))
    print(timeit.timeit(lambda: fibonacci_2(n),number=1))
