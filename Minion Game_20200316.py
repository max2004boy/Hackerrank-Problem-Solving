# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:58:28 2020

@author: max20
"""

def minion_game(string):
    # your code goes here
    vowel_list = ['a','A','e','E','i','I','o','O','u','U']
    string_len = len(string)
    Stuart_score = 0
    Kevin_score = 0

    # i is the position of the first letter of substring
    for i in range(string_len):            
        if string[i] in vowel_list:
            Kevin_score+=(string_len-i) # No need to loop through all substrings
        else:
            Stuart_score+=(string_len-i) # No need to loop through all substrings
    
    if Kevin_score>Stuart_score:
        print('Kevin', Kevin_score)
    elif Kevin_score==Stuart_score:
        print('Draw')
    else:
        print('Stuart', Stuart_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)