# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:09:38 2020

@author: max20
"""

import math
import os
import random
import re
import sys

def makeAnagram(a, b):
    joint_set = set(a).union(set(b))
    count_to_keep = 0
    for item in joint_set:
        count_to_keep+=min(a.count(item), b.count(item))
    return len(a)+len(b)-2*count_to_keep

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()