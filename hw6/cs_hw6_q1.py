from DoublyLinkedList import *

# Question 1: Define a LinkedQueue class that implements the Queue ADT.
"""
Implementation Requirement: All queue operations should run in theta(1) worst-case.
Hint: You would want to use a doubly linked list as a data member.
"""


class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def enqueue(self, elem):
        self.data.add_last(elem)

    def dequeue(self):
        if self.is_empty():  # does it matter if it's None or empty check
            raise Exception("Queue is empty")
        return self.data.delete_first()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.header.next.data  # why tho
