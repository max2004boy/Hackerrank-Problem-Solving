# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 00:44:38 2020

@author: max20
"""
import datetime as dt

def fibo_1(s):
    if s<=0:
        return 'Error'
    elif s==1:
        return 0
    elif s==2:
        return 1
    else:
        return fibo_1(s-1)+fibo_1(s-2)
    
def fibo_2(s):
    if s<=0:
        return 'Error'
    elif s==1:
        return 0
    elif s==2:
        return 1
    else:
        counter=2
        lower = 0
        upper = 1
        while counter<s:
            fibo = lower + upper
            lower = upper
            upper = fibo
            counter+=1
        return fibo

def fibo_3(s):
    if s<=0:
        return 'Error'
    elif s==1:
        return 0
    elif s==2:
        return 1
    else:
        counter=2
        fibo_list = [0,1]
        while counter<s:
            fibo_list.append(fibo_list[counter-2]+fibo_list[counter-1])
            counter+=1
        return fibo_list[counter-1]

if __name__=='__main__':
    
    target_index = 30
    
    start_1 = dt.datetime.now()
    for i in range(target_index):
        print(fibo_1(i+1))
    
    start_2 = dt.datetime.now()
    for i in range(target_index):
        print(fibo_2(i+1))
    
    start_3 = dt.datetime.now()
    for i in range(target_index):
        print(fibo_3(i+1))
    
    final_time = dt.datetime.now()
    
    print(start_2 - start_1)
    print(start_3 - start_2)
    print(final_time - start_3)
            
        