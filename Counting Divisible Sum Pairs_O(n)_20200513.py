# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:09:50 2020

@author: max20
"""

# Problem: You are given an array of integers (size n) and a positive integer k.
#          Find and print the number of unordered pairs where the sum is divisible by k.

# O(n) time comlexity (better than the double for-loop)
# we can use this algorithm because we don't have to print the pairs
# just the count
def divisibleSumPairs(n, k, ar):
    
    mod_count = [0] * k
    # count the number of elements with each mod result
    # the mod result can take values of 0,1,2,...,k-1
    for i in range(n):
        mod_count[ar[i] % k] += 1 
    
    count = 0
    for i in range(int(k/2) + 1):
        # a mod=0 element needs to be paired with another mod=0 element
        # the number of such pairs is x*(x-1)/2
        if i == 0:
            count += int(mod_count[0] * (mod_count[0] - 1) / 2)
        # a mod=k/2 element needs to be paired with another mod=k/2 element
        # only happens when k is even
        # similarly, the number of such pairs is x*(x-1)/2
        elif float(i) == (k/2):
            count += int(mod_count[int(k/2)] * (mod_count[int(k/2)] - 1) / 2)
        # for all other cases, a mod=i element nees to be paired with a mod=k-i element
        # the number of such pairs is x*y
        else:
            count += int(mod_count[i] * mod_count[k-i])     
    
    return count

# O(n^2) time complexity
def divisibleSumPairs2(n, k, ar):
    ar_sorted = sorted(ar)
    count = 0
    for i in range(len(ar_sorted)-1):
        for j in range(i+1, len(ar_sorted)):
            if (ar_sorted[i]+ar_sorted[j])% k == 0:
                count += 1
    return count
        

if __name__ == '__main__':

    n, k = map(int, input().split())
    ar = list(map(int, input().rstrip().split()))

    print('Number of such pairs:', divisibleSumPairs(n, k, ar))
