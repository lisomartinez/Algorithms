# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:37:06 2020

@author: lisan
"""

from DoublyLinkedList import DoublyLinkedList

class Stack():
    
    def __init__(self):
        self.stack = DoublyLinkedList()
    
    def push(self, k):
        self.stack.insert_first(k)
    
    def pop(self):
        if self.stack.empty() is False:
            self.stack.delete_first()
            
    def top(self):
        if self.stack.empty() is True:
            return None
        return self.stack.first()
    
    def size(self):
        return self.stack.size()
    
    def empty(self):
        return self.stack.empty()
    