# -*- coding: utf-8 -*-
"""
Created on Sun May 24 23:56:35 2020

@author: max20
"""

def circularArrayRotation(a, k, queries):
    output_num = []
    for i in queries:
        # also understand the modulo operation of negative numbers
        # e.g. -1 % 3 = 2
        output_num.append(a[(i-k) % len(a)])
    
    return output_num

if __name__ == '__main__':
    # n is the number of elements in the integer array
    # k is the rotation count
    # q is the number of queries
    n, k, q = map(int, input().split())

    a = list(map(int, input().rstrip().split()))

    queries = []
    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    print('\n'.join(map(str, result)))