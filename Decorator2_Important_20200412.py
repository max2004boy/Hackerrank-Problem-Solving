# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:44:19 2020

@author: max20
"""

def person_lister(f):
    def inner(people):
        # complete the function
        return [f(x) for x in sorted(people, key=lambda a: int(a[2]))]

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')