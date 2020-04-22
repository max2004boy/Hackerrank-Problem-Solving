# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:04:54 2020

@author: max20
"""



if __name__ == '__main__':
    n = int(input())
    bin_n = '{0:b}'.format(n)
    
    counter = 0
    counter_temp = 0
    for i in range(len(bin_n)):
        if bin_n[i]=='1':
            counter_temp+=1
            if i!=(len(bin_n)-1) and bin_n[i+1]!='1':
                if counter_temp>counter:
                    counter = counter_temp
                counter_temp = 0
            if i==(len(bin_n)-1) and counter_temp>counter:
                counter = counter_temp
    
    print(counter)
    
