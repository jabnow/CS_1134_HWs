# Question 5: Permutations implementation with stacks, queues

from current_hw.ArrayStack import ArrayStack
from current_hw.ArrayQueue import ArrayQueue

"""
Implementation Requirements:
1. Your implementation should be non-recursive.
2. Your implementation is allowed to use a Stack, a Queue, and theta(1) additional
space.

Hint: Use the stack to store the elements yet to be used to generate the
permutations and use the queue to store the (partial) collection of permutations
generated so far.
"""


def permutations(lst):
    stack = ArrayStack()
    q = ArrayQueue()
    result = []

    q.enqueue((lst, []))
    while not q.is_empty():
        rest, perm = q.dequeue()
        if not rest:
            result.append(perm)

        for i in range(len(rest)):
            next_ele = rest[:i] + rest[i + 1:]
            q.enqueue((next_ele, [rest[i]] + perm))

    return result


# Test the function
lst = [1, 2, 3]
print(permutations(lst))

# SEE THE COMBOS
# import itertools
# print(list(itertools.permutations([1, 2, 3]))
