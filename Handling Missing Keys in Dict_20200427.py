# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:57:40 2020

@author: max20
"""

def checkMagazine(magazine, note):
    note_dict = {}
    flag = 'Yes'
    for word in magazine:
        note_dict[word] = note_dict.setdefault(word, 0) + 1
    for word in note:
        note_dict[word] = note_dict.setdefault(word, 0) - 1
        if note_dict[word]<0:
            flag = 'No'
    print(flag)


if __name__ == '__main__':
    
    m, n = map(int, input().split())
    magazine = input().rstrip().split()
    note = input().rstrip().split()

    checkMagazine(magazine, note)