# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:58:26 2020

@author: max20
"""

def happyLadybugs(b):
    # count bugs with a dictionary
    bug_count = {}
    for i in range(len(b)):
        bug_count[b[i]] = bug_count.setdefault(b[i], 0) + 1

    result = 'YES'
    # if there is no empty space to move the bugs ('_')
    # check if the string is a happy bug string
    if '_' not in b:
        for i in range(len(b)):
            if len(b) > 1:
                if i == 0:
                    if b[i] != b[i + 1]:
                        result = 'NO'
                elif i == len(b) - 1:
                    if b[i] != b[i - 1]:
                        result = 'NO'
                else:
                    if b[i] != b[i - 1] and b[i] != b[i + 1]:
                        result = 'NO'
            else:
                result = 'NO'
    else:
        for j in bug_count:
            if j != '_' and bug_count[j] == 1:
                result = 'NO'
    return result
                  

if __name__ == '__main__':

    n = int(input())
    b = input()
    print(happyLadybugs(b))