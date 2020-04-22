# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 00:40:14 2020

@author: max20
"""

if __name__ == '__main__':
    students = []
    scores = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)
    
    second_low_score = sorted(scores)[1]
    
    second_low_student = []
    for item in students:
        if item[1] == second_low_score:
            second_low_student.append(item[0])
    
    for item in sorted(second_low_student):
        print(item)
    
    