from DoublyLinkedList import DoublyLinkedList
from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

# Question 1
"""
Give the preorder, postorder, and inorder traversal sequences, for the following binary tree:

   ___1  
  /    \ 
 _2    7 
/  \    \
5  4_   8
 \   \   
 6   3   
    /    
    9

Recursive Traversals
Preorder:  1 2 5 6 4 3 9 7 8  (D, L, R)
Postorder: 6 5 9 3 4 2 8 7 1  (L, R, D)
Inorder:   5 6 2 4 9 3 1 7 8  (L, D, R)

L = recursive call on left subtree
R = recursive call on right subtree
D = process node
"""

# Question 2
"""
Part a)
Operations: 1 2 3 4 + 5 - * +

                  4   5
                3 3 7 7 2
              2 2 2 2 2 2 4 
Stack:      1 1 1 1 1 1 1 1 5

Algorithm: if number, push to stack
           if operator, pop 2 numbers, do calculation, push result to stack

Part b)
Recommend converting to infix first so you can see the order of operations

postfix: 1 2 3 4 + 5 - * +
infix:   (1 + (2 * ((3 + 4) - 5)))
prefix:  + 1 * 2 - + 3 4 5

Can't just reverse the postfix since not all operators are commutative (subtraction and division)!
if we did reverse the postfix, we would get:
prefix:  + * - 5 + 4 3 2 1
infix:   (((5 - (4 + 3)) * 2) + 1)
"""

# Question 3
def move_to_end(self, node):
    if node == self.trailer.prev:
        return

    # reorder prev and next nodes
    prev_node = node.prev
    next_node = node.next

    prev_node.next = next_node
    next_node.prev = prev_node

    # modify node and trailer
    prev_node = self.trailer.prev
    next_node = self.trailer

    prev_node.next = node
    node.prev = prev_node
    node.next = next_node
    next_node.prev = node

# Testing Q3
# Don't do this in practice, just doing it here so
# we don't have to copy paste the entire
# DoublyLinkedList class definition
DoublyLinkedList.move_to_end = move_to_end

dll = DoublyLinkedList()
for i in range(10):
    dll.add_last(i)
print(f"DLL before moving:   {dll=}")
dll.move_to_end(dll.header.next.next.next) # 2
print(f"DLL after moving 2:  {dll=}") # 0 1 3 4 5 6 7 8 9 2
dll.move_to_end(dll.header.next) # 0
print(f"DLL after moving 0:  {dll=}") # 1 3 4 5 6 7 8 9 2 0
dll.move_to_end(dll.trailer.prev) # 0
print(f"DLL after moving 0:  {dll=}") # 1 3 4 5 6 7 8 9 2 0
dll.move_to_end(dll.trailer.prev.prev.prev) # 9
print(f"DLL after moving 9:  {dll=}") # 1 3 4 5 6 7 8 2 0 9


# Question 4
# alternate even, odd, even, odd, etc.
def alternating_parity(lst):
    evens = ArrayStack()
    odds  = ArrayQueue()

    for num in lst:
        if num % 2 == 0:
            evens.push(num)
        else:
            odds.enqueue(num)

    # since stack is lifo, we want to start at the end of the list
    # lifo = last in first out
    even_index = len(lst) - 2
    while not evens.is_empty():
        lst[even_index] = evens.pop()
        even_index -= 2

    # since queue is fifo, we want to start at the beginning of the list
    # fifo = first in first out
    odd_index  = 1
    while not odds.is_empty():
        lst[odd_index] = odds.dequeue()
        odd_index += 2

# Testing Q4
def test_alternating(lst):
    print(f"Before alternating: {lst=}")
    alternating_parity(lst)
    print(f"After alternating:  {lst=}")

for lst in [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 2],
            [2, 1],
            []]:
    test_alternating(lst)


# Question 5
# hint: since all operations must be worst case O(1), not amortized O(1), cannot use ArrayList/ArrayStack/ArrayQueue
# which are amortized O(1) due to resizing
class FlippableStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.flipped = False
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self, val):
        if self.flipped:
            self.data.add_last(val)
        else:
            self.data.add_first(val)
    
    def pop(self):
        if self.is_empty():
            raise Exception("FlippableStack is empty")
        if self.flipped:
            return self.data.delete_last()
        else:
            return self.data.delete_first()

    def top(self):
        if self.is_empty():
            raise Exception("FlippableStack is empty")
        if self.flipped:
            return self.data.trailer.prev.data
        else:
            return self.data.header.next.data

    def flip(self):
        self.flipped = not self.flipped
    
    def __repr__(self):  # for demonstration purposes only
        return str(self.data)

# Part B: see pdf for memory image

# Testing Q5
fs = FlippableStack()
for i in range(5):
    fs.push(i)
print(f"Before any operations:  {fs=}")
print(f"Top of flippable stack: {fs.top()=}") # 4
fs.flip()
print(f"After flip:             {fs=}")
print(f"Top of flippable stack: {fs.top()=}") # 0
for i in range(5, 10):
    fs.push(i)
print(f"After pushing 5-10:     {fs=}")
print(f"Top of flippable stack: {fs.top()=}") # 9
fs.flip()
print(f"After flip:             {fs=}")
print(f"Top of flippable stack: {fs.top()=}") # 4
