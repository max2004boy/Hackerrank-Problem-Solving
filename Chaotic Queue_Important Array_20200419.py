# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:46:19 2020

@author: max20
"""

def minimumBribes(q):
    total_disorder = 0
    for i in range(0,len(q)):
        # check if q[i] has moved too far (i.e. >2)
        move_forward = q[i] - i - 1
        if move_forward>2:
            print('Too chaotic')
            return
        else: 
            # count how many numbers bigger than q[i] have passed it
            # start from max(0, q[i]-2) significantly improves efficiency!!!
            disorder_temp = sum([x>q[i] for x in q[max(0, q[i]-2):i]])
            total_disorder+=disorder_temp
    
    print(total_disorder)
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)