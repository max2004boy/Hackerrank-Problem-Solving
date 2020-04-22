# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 00:35:33 2020

@author: max20
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    gmail_namelist = []
    
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        if re.search('@gmail\.com$', emailID):
            gmail_namelist.append(firstName)
    
    print(*sorted(gmail_namelist), sep='\n')
    
