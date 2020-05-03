# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:07:09 2020

@author: max20
"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root):
    # check whether the root/node exists
    if root==None:
        return -1
    else:
        # recursion to get tree height
        return max(height(root.left), height(root.right)) + 1


if __name__ == '__main__':
    
    tree = BinarySearchTree()
    t = int(input())
    
    arr = list(map(int, input().split()))
    
    for i in range(t):
        tree.create(arr[i])
    
    print('The height of the Binary Search Tree is:', height(tree.root))
