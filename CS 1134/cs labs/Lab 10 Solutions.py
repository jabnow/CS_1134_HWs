from DoublyLinkedList import DoublyLinkedList
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

#Question 1

class LinkedStack:

    def __init__(self):
        self.data = DoublyLinkedList()
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self, e):
        self.data.add_last(e)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty!")
        return self.data.delete_last()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is Empty!")
        return self.data.trailer.prev.data
        
'''
s = LinkedStack()
s.push(5)
s.pop()
s.push(10)
s.push(12)
s.push(6)
s.push(6)

print(s.data)
print(s.top())
'''

#Question 2

class DLL(DoublyLinkedList): #ignore this part

    #just look at the method below, here 
    #add this part to the DoublyLinkedList implementation from class

    def __getitem__(self, ind):
    
        if 0 <= ind <= len(self)//2 : #if ind is in first half, start from header

            start = self.header.next              #first node (index 0)
            for i in range(ind):
                start = start.next                #bump the pointer to next

            return start.data
        
        elif len(self)//2 < ind < len(self): # if ind in second half, start from trailer

            start = self.trailer.prev             #last node (index  = len(lst) - 1)
            for i in range(len(self)-1, ind, -1): #iterate backwards
                start = start.prev                #bump the pointer backwards

            return start.data

        else: #out of bounds
            raise IndexError("Index out of range!")



'''
DoublyLinkedList = DLL

dll = DoublyLinkedList()
dll.add_last(5)
dll.add_last(2)
dll.add_first(6)
dll.add_last(8)
dll.add_first(10)
dll.add_first(4)
dll.add_last(1)
print(dll)

for i in range(len(dll)):
    print(dll[i])






print("compiled successfully")
'''

#Question 3

class MidStack:

    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = None #starts off None for empty DLL

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0
    

    def push(self, e):
        self.data.add_last(e) #add to top of stack

        if len(self) == 1: #only 1 element (was empty before)
            self.mid = self.data.trailer.prev #mid is last node 
        
        elif len(self) % 2 != 0: #if len is odd, bump pointer up
            self.mid = self.mid.next


    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        val = self.data.delete_last()

        if self.is_empty():
            self.mid = None

        elif len(self) % 2 == 0: #if len is even, bump pointer down
            self.mid = self.mid.prev
        
        return val
    

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.data.trailer.prev.data
    

    def mid_push(self, e):
        self.data.add_after(self.mid, e) #add to top of stack

        if len(self) == 1: #only 1 element (was empty before)
            self.mid = self.data.trailer.prev #mid is last node 
        
        elif len(self) % 2 != 0: #if len is odd, bump pointer up
            self.mid = self.mid.next


    def get_mid(self): #optional
        return self.mid.data

'''
ms = MidStack()
print("Here")
ms.push(5)
print(ms.data, ms.get_mid())
ms.push(3)
print(ms.data, ms.get_mid())
ms.push(2)
print(ms.data, ms.get_mid())
ms.push(4)
print(ms.data, ms.get_mid())
ms.push(1)
print(ms.data, ms.get_mid())
ms.mid_push(8)
print(ms.data, ms.get_mid())
ms.mid_push(10)
print(ms.data, ms.get_mid())
ms.pop()
print(ms.data, ms.get_mid())
ms.pop()
print(ms.data, ms.get_mid())
'''

#Question 4

class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next
            
        def disconnect(self):
            self.data = None
            self.next = None

    def __init__(self): 
        self.header = None  # points to actual node, NOT sentinel
        self.tail   = None  # points to actual node, NOT sentinel
        self.size   = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        ''' Creates a new node containing val as its data and adds it after an existing node in the SinglyLinkedList'''
        if self.is_empty():
            raise Exception("Cannot add after node because SLL is empty")

        curr_node = node
        next_node = curr_node.next

        new_node = SinglyLinkedList.Node(val, next_node)
        curr_node.next = new_node

        # if the curr_node is the last node (tail), then new_node is the new tail
        if curr_node is self.tail:
            self.tail = new_node
        
        self.size += 1

    def add_first(self, val):
        ''' Creates a new node containing val as its data and adds it to the front of the SinglyLinkedList'''
        new_node = SinglyLinkedList.Node(val)
        if self.is_empty():  # edge case, empty SLL. Both header and tail are None
            self.header = new_node
            self.tail   = new_node
        else:  # Why can't we use add_after() here? - no node before self.header
            new_node.next = self.header
            self.header = new_node
        
        self.size += 1

    def add_last(self, val):
        ''' Creates a new node containing val as its data and adds it to the back of the SinglyLinkedList'''
        new_node = SinglyLinkedList.Node(val)
        if self.is_empty():  # edge case, empty SLL. Both header and tail are None
            self.header = new_node
            self.tail   = new_node
            self.size   += 1
        else:  # What if we didn't have self.tail?
            self.add_after(self.tail, val)  # add_after updates size

    def delete_first(self):
        ''' Removes an existing node from the front of the SinglyLinkedList and returns its value'''
        if self.is_empty():
            raise Exception("Trying to remove from an empty SLL")

        curr_node = self.header  # Header/tail are NOT sentinel nodes

        self.header = curr_node.next
        if curr_node is self.tail:
            self.tail = curr_node.next  # aka, None
        
        val = curr_node.data
        curr_node.disconnect()
        self.size -= 1
        return val

    def delete_last(self):
        ''' Removes an existing node from the back of the SinglyLinkedList and returns its value'''
        if self.is_empty():
            raise Exception("Trying to remove from an empty SLL")
        # Need to get node before self.tail
        # How do we get the second to last element? - Need to loop

        if len(self) == 1:
            curr_node = self.header
            self.header = self.tail = None
            val = curr_node.data
            curr_node.disconnect()
            return val
        
        # Else size > 1
        prev_node = self.header     # Has to be some Node since SLL is at least size 1
        curr_node = prev_node.next  # Has to be some Node since SLL is at least size 2
        while curr_node is not self.tail:
            prev_node, curr_node = curr_node, curr_node.next  # Move pointers up

        val = curr_node.data
        prev_node.next = curr_node.next
        curr_node.disconnect()

        self.tail = prev_node
        self.size -= 1
        return val

    def reverse(self):
        '''Reverses the list using node pointers and returns the new head. Solution must use constant space-complexity'''
        if self.is_empty():
            return

        prev = None
        curr = self.header

        while curr is not None:
            next = curr.next
            curr.next = prev
            curr, prev = next, curr

        # Update header
        self.header = prev

    def __iter__(self):
        cursor = self.header
        while(cursor is not None):
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " -> ".join([str(elem) for elem in self]) + "]"
