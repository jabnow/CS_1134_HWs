# Question 2: MaxStack ADT
"""
Assume that the user inserts only integers to this stack

1. For the representation of MaxStack objects, your data members should be:
• A Stack – of type ArrayStack
• Additional theta(1) space - for additional data members, if needed

2. Your implementation should support the max operation in theta(1) worst-case time.
For all other Stack operation, the running time should remain as it was in the
original implementation.

Hint: You may want to store a tuple, as elements of the ArrayStack. That is, to
attach to every “real” data in this stack some additional information.
"""

import ArrayDeque
from ArrayStack import ArrayStack
import ArrayList
import ArrayQueue


class MaxStack:
    def __init__(self):
        """initializes an empty MaxStack object"""
        self.maxS = ArrayStack()
        self.max_val = None

    def is_empty(self):
        """returns True if maxS does not contain any elements,
or False otherwise."""
        return len(self.maxS) == 0

    def __len__(self):
        """Returns the number of elements in maxS"""
        return len(self.maxS)

    def push(self, e):
        """adds element e to the top of maxS."""
        if self.max_val is None or e > self.max_val:
            self.max_val = e
        self.maxS.push((e, self.max_val))

    def top(self):
        """maxS.top(): returns a reference to the top element of maxS, without
removing it; an exception is raised if maxS is empty."""
        if self.maxS.is_empty():
            raise Exception("stack is empty")
        temp = self.maxS.top()[0]
        return temp

    def pop(self):
        """removes and return the top element from maxS; an exception
is raised if maxS is empty."""
        if self.is_empty():
            raise Exception("stack is empty")
        bob = self.maxS.pop()
        val = self.maxS.top()
        self.max_val = val[1]
        return bob[0]

    def max(self):
        """maxS.max(): returns the element in maxS with the largest value, without
removing it; an exception is raised if maxS is empty."""
        if self.maxS.is_empty():
            raise Exception("stack is empty")
        return self.max_val

