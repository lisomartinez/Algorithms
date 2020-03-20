# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:13:42 2020

@author: lisan
"""

class Node():
    
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.value = val

class DoublyLinkedList():
    
    def __init__(self):
        sentinel = Node(None)
        sentinel.prev = sentinel.next
        sentinel.next = sentinel.prev
        self.root = sentinel
        self.size = 0
    
    def search(self, k):
        x = self.root.next
        while x is not self.root and x.value is not k:
            x = x.next
        return x
    
    def insert_first(self, k):
        x = Node(k)
        x.next = self.root.next
        self.root.next.prev = x
        self.root.next = x
        x.prev = self.root
        self.size += 1
        
    def insert_last(self, k):
        x = Node(k)
        x.prev = self.root.prev
        self.root.prev.next = x
        self.root.prev = x
    
    def delete_first(self):
        if self.root.next is self.root.prev:
            return
        self.root.next.next.prev = self.root.next 
        self.root.next = self.root.next.next
    
    def delete_last(self):
        if self.root.next is self.root.prev:
            return
        self.root.prev.prev.next = self.root.prev
        self.root.prev = self.root.prev.prev
    
    def delete(self, k):
        x = self.search(k)
        if x is None:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1
        
    def first(self):
        if self.size == 0:
            return None
        return self.root.next
        
    def size(self):
        return self.size
    
    def empty(self):
        return self.size == 0