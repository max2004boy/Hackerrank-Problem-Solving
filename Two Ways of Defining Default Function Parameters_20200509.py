# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:29:06 2020

@author: max20
"""

# First way to set default values
# the default value is only evaluated once at definition
test_a = 10

def print_test1(i=test_a):
    print(i)

test_a += 10
# this will only print 10
print_test1()




# Second way to set default values (to None)
test_b = 10

def print_test2(i=None):
    # use if condition to put in the actual "default value"
    if i==None:
        i = test_b
        print(i)
    else:
        print(i)

test_b += 10
# this will print 20
print_test2()