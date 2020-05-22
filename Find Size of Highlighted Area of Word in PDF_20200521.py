# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:28:52 2020

@author: max20
"""

def designerPdfViewer(h, word):
    # create dictionary of character heights
    h_dict = {}
    j = 0
    for i in range(ord('a'),ord('a')+26):
        h_dict[chr(i)] = h[j]
        j += 1
    
    # find maximum height of characters in the word
    h_max = max([h_dict[k] for k in word])
    
    # find the highlighted area of the word
    return h_max*len(word)

if __name__ == '__main__':

    h = list(map(int, input().rstrip().split())) # list of heights for the 26 characters
    word = input()
    print(designerPdfViewer(h, word))