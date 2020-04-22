# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:34:55 2020

@author: max20
"""

import os

def diagonalDifference(arr):
    # Write your code here
    diag_a = 0
    diag_b = 0
    for i in range(len(arr)):
        diag_a += arr[i][i]
        diag_b += arr[i][-i-1]
    
    return abs(diag_a - diag_b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()