# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:18:06 2020

@author: max20
"""

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []
    
    def pushCharacter(self, ch):
        self.stack.append(ch)
    
    def enqueueCharacter(self, ch):
        self.queue.append(ch)
    
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        item_temp = self.queue[0]
        del self.queue[0]
        return item_temp


# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")  