# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:49:55 2020

@author: max20
"""

import math
import os
import random
import re
import sys


def isValid(s):
    counts = []
    for test_char in set(s):
        counts.append(s.count(test_char))
    
    min_count = min(counts)
    max_count = max(counts)

    if min_count==1 and counts.count(max_count)>=len(set(s))-1:
        return 'YES'
    elif max_count-min_count<=1 and counts.count(min_count)>=len(set(s))-1:
        return 'YES'
    else:
        return 'NO'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
