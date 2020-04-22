# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:13:00 2020

@author: max20
"""

def fun(s):
    # return True if s is a valid email, else return False
    if s.find('@')<=0 or s.find('.')<=1:
        return False
    else:
        username_temp = s[:s.find('@')]
        if len(list(filter(lambda x: x.isalnum() or x=='_' or x=='-', list(username_temp))))!= len(username_temp):
            return False

        website_temp = s[(s.find('@')+1):s.find('.')]
        if not website_temp.isalnum():
            return False
        
        extension_temp = s[(s.find('.')+1):]
        if len(extension_temp)>3:
            return False

    return True
        


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)