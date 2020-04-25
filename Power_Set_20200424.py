# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:47:32 2020

@author: max20
"""

def power_set(s=set()):
    set_len = len(s)
    power_set_all = set()
    
    for i in range(set_len+1):
        
        if i==0:
            power_set_tmp = {frozenset()}
            power_set_all = power_set_all.union(power_set_tmp)
            power_prev = power_set_tmp
            
        else:
            power_set_tmp = set()
            for m in power_prev:
                for n in s:
                    if (n not in m) and (frozenset(m.union(set(n))) not in power_set_tmp):
                        power_set_tmp.add(frozenset(m.union({n})))
            power_set_all = power_set_all.union(power_set_tmp)
            power_prev = power_set_tmp
    
    return power_set_all



if __name__ == '__main__':
    
    input_set = set(input().split())
    print(power_set(input_set))