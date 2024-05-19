from DoublyLinkedList import DoublyLinkedList
from LinkedBinaryTree import LinkedBinaryTree
from ChainingHashTableMap import ChainingHashTableMap
from ArrayQueue import ArrayQueue


# 1
'''
a.
Inserting 6: 6 goes to the left of 7
Deleting 13: 11 replaces 13, subtree looks like the following:
        ... (rest  of the tree)
        ...
                11
        7               15
            9                 19
                          17

b.
Inorder(T): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Postorder(T): 1, 3, 4, 2, 5, 8, 7, 9, 11, 10, 6
            6
        5         10
    2           9    11
1      4      7
     3         8
'''


# 2
'''
a.
      +
  2       *
        3   +
          4   5


b. 
      +
  4      **
        3  2


c.
      *
  +       -
2   3   4   5
'''


# 3
def remove_dups(lst):
    map = ChainingHashTableMap()
    ptr = lst.header.next
    while ptr is not lst.trailer:
        num = ptr.data
        if num not in map:
            map[num] = None
            ptr = ptr.next
        else:
            node_to_delete = ptr
            ptr = ptr.next
            lst.delete_node(node_to_delete)


# 4
def is_size_tree(bin_tree):
    def helper(root):
        if not root:
            return 0, True
        left_size, is_left = helper(root.left)
        right_size, is_right = helper(root.right)
        curr_size = left_size + right_size + 1
        return curr_size, (is_left and is_right and curr_size == root.data)

    size, boolean = helper(bin_tree.root)
    return boolean


# 5
class ExtendedPartiesQueue:
    def __init__(self):
        self.q = ArrayQueue()
        self.map = ChainingHashTableMap()

    def __len__(self):
        return len(self.q)

    def enq_party(self, party_name, party_size):
        self.q.enqueue(party_name)
        self.map[party_name] = party_size

    def add_to_party(self, party_name, size_to_add):
        if party_name not in self.map:
            raise Exception("No party name found with name:", party_name)
        self.map[party_name] += size_to_add

    def first_party(self):
        party_name = self.q.first()
        return self.map[party_name]

    def deq_first_party(self):
        party_name = self.q.dequeue()
        size = self.map[party_name]
        del self.map[party_name]
        return size

