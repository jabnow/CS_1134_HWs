from ArrayDeque import ArrayDeque
from current_hw.ArrayStack import ArrayStack

# Question 3: MidStack ADT

"""
1. For the representation of MidStack objects, your data members should be:
• A Stack – of type ArrayStack
• A double ended queue – of type ArrayDeque
• Additional theta(1) space - for additional data members, if needed

2. Your implementation should support the mid_push operation in theta(1)
amortized time. For all other Stack operation, the running time should remain as
it was in the original implementation (That is, theta(1) amortized for push and pop,
and theta(1) worst-case for top, len and is_empty).
"""


class MidStack:
    def __init__(self):
        # initializes an empty MidStack object
        self.stack = ArrayStack()
        self.deque = ArrayDeque()

    def is_empty(self):
        """returns True if S does not contain any elements, or
False otherwise."""
        return len(self.stack) == 0 and len(self.deque) == 0

    def __len__(self):
        # Returns the number of elements midS
        return len(self.stack) + len(self.deque)

    def push(self, e):
        # adds element e to the top of midS.
        self.stack.push(e)
        if len(self.deque) > len(self.stack):
            self.stack.push(self.deque.dequeue_first())

    def top(self):
        """returns a reference to the top element of midS, without
removing it; # an exception is raised if midS is empty."""
        # so like copy, no copy??
        if self.stack.is_empty():
            raise Exception("MidStack is empty")
        if self.deque.is_empty():
            return self.stack.top()
        return self.deque[-1]

    def pop(self):
        """removes and returns the top element from midS; an
        exception is raised if midS is empty."""
        if self.is_empty():
            raise Exception("MidStack is empty")
        if len(self.stack) > len(self.deque):
            self.deque.enqueue_first(self.stack.pop())
        return self.deque.dequeue_last()

    def mid_push(self, e):
        """That is, assuming there are n elements in S: In the case n is even, e would go
        exactly in the middle. If n is odd, e will go after the (n+1)/2 th element."""
        mid_ind = len(self.stack) // 2
        for i in range(mid_ind):
            self.deque.enqueue_first(self.stack.pop())
        self.stack.push(e)
        while not self.deque.is_empty():
            self.stack.push(self.deque.dequeue_first())


"""
ANOTHER PROBLEM WITH POP
line 53
Exception: stack is empty


Test pushing example elements
Test popping elements to ensure push order
Test Failed: 2 != 8
"""