#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:19:31 2018

@author: karthikeyan sankar
"""

#Binary tree
#   tree
#   ----
#     1
#    / \
#   2   3
#  /
# 4
# Program to create simp
class Node:
    def __init__(self,val):
        self.value = val
        self.right = None
        self.left  = None
class BinaryTree:
    def __init__(self,val):
        self.root  = Node(val)
    def insert(self, data):
        temp = Node(data)
                
#root = Node(1)
x = BinaryTree(1)
x.root.left=Node(2)
x.root.right=Node(3)
x.root.left.left=Node(4)