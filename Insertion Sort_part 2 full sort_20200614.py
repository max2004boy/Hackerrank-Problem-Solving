# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 20:06:20 2020

@author: max20
"""
# https://www.hackerrank.com/challenges/insertionsort2/problem

# time complexity is O(n^2)
def insertionSort2(n, arr):
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            insert_num = arr[i+1]
            for j in range(i, -1, -1):
                if arr[j] > insert_num:
                    arr[j + 1] = arr[j]
                    # if the number to insert happens to be the smallest
                    if j == 0:
                        arr[j] = insert_num
                else:
                    # insert the number at the correct location found
                    arr[j + 1] = insert_num
                    break
        # print array after each iteration (i)
        print(*arr)

if __name__ == '__main__':
    
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)