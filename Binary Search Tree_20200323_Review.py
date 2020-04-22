# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:52:24 2020

@author: max20
"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if root:
            leftDepth = self.getHeight(root.left)
            rightDepth = self.getHeight(root.right)
            return max(leftDepth,rightDepth) + 1
        else:
            return -1
    
    def levelOrder(self,root):
        #Write your code here
        node_list = [root] if root else []
        
        while node_list:
            node_to_print = node_list.pop()
            print(node_to_print.data, end=' ')

            if node_to_print.left:
                node_list.insert(0, node_to_print.left)
        
            if node_to_print.right:
                node_list.insert(0, node_to_print.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       