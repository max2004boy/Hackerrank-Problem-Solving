# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:53:02 2020

@author: max20
"""

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    a_in_s = s.count('a')
    quotient = n//len(s)
    remainder = n%len(s)
    a_in_remainder = s[:remainder].count('a')
    
    return a_in_s*quotient + a_in_remainder

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()