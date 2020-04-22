# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:43:54 2020

@author: max20
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        if head==None:
            head = Node(data)
        else:
            new_node = Node(data)
            current = head
            while current.next!=None:
                current = current.next
            
            current.next = new_node
            
        return head
        
    def insert_recursion(self,head,data):
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else: 
            self.insert(head.next, data)
        
        return head
     
    def removeDuplicates(self,head):
        #Write your code here
        if head!=None:
            current = head
            data_list = [current.data]
            while current.next:
                if current.next.data not in data_list:
                    data_list.append(current.next.data)
                    current = current.next
                else:
                    current.next = current.next.next
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  