# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:00:47 2020

@author: lisan
"""

from DoublyLinkedList import DoublyLinkedList

class Queue():
    
    def __init__(self):
        self.queue = DoublyLinkedList()
    
    def enqueue(self, k):
        self.queue.insert_last(k)
        
    def dequeue(self):
        self.queue.delete_first
    
    def first(self):
        if self.queue.empty() is True:
            return None
        return self.queue.first()
    
    def size(self):
        return self.queue.size()
    
    def empty(self):
        return self.queue.empty()