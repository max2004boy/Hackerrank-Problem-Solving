# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:24:03 2020

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


def lca(root, v1, v2):
  # check for where the "split" happens between v1 and v2
  lca_node = root
  
  while True:
    if v1<lca_node.info and v2<lca_node.info:
        lca_node = lca_node.left      
    elif v1>lca_node.info and v2>lca_node.info:
        lca_node = lca_node.right     
    else:
        return lca_node

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)