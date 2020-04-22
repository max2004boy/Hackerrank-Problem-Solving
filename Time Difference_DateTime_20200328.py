# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:35:01 2020

@author: max20
"""

import math
import os
import random
import re
import sys
import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    month_dic = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

    t1_list = list(t1.split())
    t2_list = list(t2.split())

    t1_time = dt.datetime(int(t1_list[3]),month_dic[t1_list[2]],int(t1_list[1]),int(t1_list[4][0:2]),int(t1_list[4][3:5]),int(t1_list[4][6:]))
    t2_time = dt.datetime(int(t2_list[3]),month_dic[t2_list[2]],int(t2_list[1]),int(t2_list[4][0:2]),int(t2_list[4][3:5]),int(t2_list[4][6:]))

    tz_1 = -int(t1_list[5][0]+str(int(t1_list[5][1:3])*3600 + int(t1_list[5][3:])*60))
    tz_2 = -int(t2_list[5][0]+str(int(t2_list[5][1:3])*3600 + int(t2_list[5][3:])*60))
    
    return str(abs(int((t1_time - t2_time).total_seconds() + (tz_1 - tz_2))))

def time_delta_2(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    return str(abs(int((dt.datetime.strptime(t1, fmt) - dt.datetime.strptime(t2, fmt)).total_seconds())))

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        delta_2 = time_delta_2(t1, t2)

        print(delta + '\n')
        print(delta_2 + '\n')


