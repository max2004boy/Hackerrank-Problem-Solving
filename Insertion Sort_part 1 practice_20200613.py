# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:38:52 2020

@author: max20
"""
# https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    insert_num = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] > insert_num:
            arr[i + 1] = arr[i]
            print(*arr)
            # if the number to insert happens to be the smallest
            if i == 0:
                arr[i] = insert_num
                print(*arr)     
        else:
            # insert the number at the correct location found
            arr[i + 1] = insert_num
            print(*arr)
            break
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)