# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:12:35 2020

@author: max20
"""

# define a help function with lower and upper boundaries
# note the low_bound and up_bound variables get updated daynamically as recursion goes deeper
# important!
def checkhelp(node, low_bound, up_bound):
    if node==None:
        return True
    elif low_bound<node.data<up_bound:
        return checkhelp(node.left, low_bound, node.data) and checkhelp(node.right, node.data, up_bound)
    else:
        return False

def checkBST(root):
    # start with the root node and -/+ infinity as the boundaries
    return checkhelp(root, float('-Inf'), float('Inf'))
        