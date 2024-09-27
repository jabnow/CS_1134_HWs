# Question 4: Give an alternative implementation for the Queue ADT.

"""
1. For the representation of Queue objects, your data members should be:
• Two Stacks – of type ArrayStack
• Additional theta(1) space - for additional data members, if needed

2. Any sequence of n enqueue and dequeue operations (starting with an empty
queue) should run in worst-case of theta(n) altogether.
"""

import ArrayDeque
from ArrayStack import ArrayStack
import ArrayList
import ArrayQueue


class Queue:
    def __init__(self):
        self.front = None
        self.stack1 = ArrayStack()  # the enqueue one
        self.stack2 = ArrayStack()  # the dequeue one

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def is_empty(self):
        return len(self.stack1) + len(self.stack2) == 0

    def first(self):        # THIS KEEPS FAILING THE OUTPUT??
        if self.is_empty():
            raise IndexError("empty")
        if self.stack2.is_empty():
            for i in range(len(self.stack1)):
                self.stack2.push(self.stack1.pop())
        return self.stack2.top()

    def enqueue(self, e):
        self.stack1.push(e)
        if self.is_empty():
            self.front = e

    def dequeue(self):
        result = None
        if self.is_empty():
            raise IndexError("empty")
        if self.stack2.is_empty():
            for i in range(len(self.stack1)):
                self.stack2.push(self.stack1.pop())
            self.front = self.stack2.top()
        return self.stack2.pop()
