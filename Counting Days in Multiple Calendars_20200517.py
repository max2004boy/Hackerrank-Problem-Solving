# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:36:34 2020

@author: max20
"""

def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.'+str(year)
    elif year < 1918:
        if year % 4 == 0:
            return '12.09.' + str(year)
        else:
            return '13.09.' + str(year)
    else:
        if (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0):
            return '12.09.' + str(year)
        else:
            return '13.09.' + str(year)

if __name__ == '__main__':

    year = int(input().strip())
    print(dayOfProgrammer(year))