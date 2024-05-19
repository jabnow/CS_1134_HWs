from LinkedBinaryTree import LinkedBinaryTree
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


Tree = LinkedBinaryTree

def build_complete_binary_tree(level):
    root = Tree.Node(0)
    q = ArrayQueue()
    q.enqueue(root)
    counter = 1
    for i in range(level):
        length = len(q)
        for j in range(length):
            node = q.dequeue()
            node.left = Tree.Node(counter)
            node.right = Tree.Node(counter + 1)
            q.enqueue(node.left)
            q.enqueue(node.right)
            counter += 2
            
    return Tree(root)

#building two complete tree
complete_tree1 = build_complete_binary_tree(2)
complete_tree2 = build_complete_binary_tree(3)


#building a full tree
root_full = Tree.Node(1, Tree.Node(2, Tree.Node(4, Tree.Node(7), 
                                              Tree.Node(6, Tree.Node(4),
                                                           Tree.Node(1))),
                                 Tree.Node(5, Tree.Node(10), 
                                              Tree.Node(10))), 

                    Tree.Node(5, Tree.Node(9), 
                                 Tree.Node(9, Tree.Node(19, Tree.Node(8), Tree.Node(8)),
                                              Tree.Node(13))))

full_tree = Tree(root_full)



#EXAMPLE TREE

'''
Tree.Node(data, left = None, right = None)

root -> left
     -> right
'''

#building the tree for better visualization
root = Tree.Node(1, Tree.Node(2, Tree.Node(4, Tree.Node(7), 
                                              Tree.Node(6, Tree.Node(4),
                                                           Tree.Node(1))),
                                 Tree.Node(5, None, 
                                              Tree.Node(10))), 

                    Tree.Node(5, None, 
                                 Tree.Node(9, Tree.Node(19, Tree.Node(8)),
                                              Tree.Node(13))))

print("Example Tree:")
bin_tree = Tree(root)
print(bin_tree)












'''
LAB ANSWERS BEGIN HERE. THEY DONT NEED TO SEE HOW THE BINARY TREES ARE BUILT. 
THE TEST CASES PRINT THEM SO THEY CAN SEE WHAT EACH ONE LOOKS LIKE. 
STUDENTS WILL NOT BE GIVEN THE CODE TO PRINT TREES UNTIL FINALS WEEK. 
THEY CAN MAKE ONE THEMSELVES IF THEY'D LIKE THOUGH! :)
    
SHOW THEM THE ANSWER CODE AND EXPLAIN HOW IT WORKS. THEN EXPLAIN THE OUTPUT.
NO NEED TO EXPLAIN THE TEST CODE.
'''



#QUESTION 1
print("\n\n\nQUESTION 1: Is Perfect Binary Trees?")
def is_perfect_recursive(root):
    if root is None: # None node is a perfect tree and has height of -1
        return (True, -1)
    
    left = is_perfect_recursive(root.left) # ( bool -> is perfect tree?, height -> integer of height)
    right = is_perfect_recursive(root.right)# ( bool -> is perfect tree?, height -> integer of height)
    
    return (left[0] and right[0] and left[1] == right[1], min(left[1], right[1]) + 1)

print("Is Complete Tree1 perfect? :", is_perfect_recursive(complete_tree1.root)[0])

print("Is Complete Tree2 perfect? :", is_perfect_recursive(complete_tree2.root)[0])

print("Is full_tree perfect? :", is_perfect_recursive(full_tree.root)[0])

print("Is bin_tree perfect? :", is_perfect_recursive(bin_tree.root)[0])


def is_perfect_iterative(root):
    
    q = ArrayQueue()
    q.enqueue(root)
    lvl = 0
    while not q.is_empty():
        if len(q) != 2**lvl: #Number nodes matches level
            return False
        for _ in range(len(q)):
            node = q.dequeue()
            
            if node.left:
                q.enqueue(node.left)
                
            if node.right:
                q.enqueue(node.right)
        lvl += 1
                
    return True
            

print("Is Complete Tree1 perfect? :", is_perfect_iterative(complete_tree1.root))

print("Is Complete Tree2 perfect? :", is_perfect_iterative(complete_tree2.root))

print("Is full_tree perfect? :", is_perfect_iterative(full_tree.root))

print("Is bin_tree perfect? :", is_perfect_iterative(bin_tree.root)) 



#QUESTION 2
print("\n\n\nQUESTION 2: Preorder with Stack")


    
    #THIS METHOD WAS WRITTEN WITHOUT "self"
def preorder_with_stack(tree):
    
    if (tree.root is not None): #the binary tree is not empty
        node = tree.root
        
        s = ArrayStack()
        s.push(node)
        
        while (not s.is_empty()):
            node = s.pop()
            yield node.data
            
            '''
            Preorder is D L R
            the Right Node must go in before the Left Node
            because the stack reverses the order they come out of
            
            '''
            
            if (node.right is not None):
                s.push(node.right)
            
            if (node.left is not None):
                s.push(node.left)
    
    
        



print("\n\nExample Complete Tree1:\n\n", complete_tree1, "\nPreorder:")
for item in preorder_with_stack(complete_tree1):
    print(item, end = ' ')
print()


print("\n\nExample Complete Tree2:\n\n", complete_tree1, "\nPreorder:")
for item in preorder_with_stack(complete_tree2):
    print(item, end = ' ')
print()


print("\n\nExample non Complete Tree:\n\n", bin_tree, "\nPreorder:")
for item in preorder_with_stack(bin_tree):
    print(item, end = ' ')
print()


print("\n\nExample Full Tree\n\n", full_tree, "\nPreorder:")
for item in preorder_with_stack(full_tree):
    print(item, end = ' ')
print()




#QUESTION 3
print("\n\n\nQUESTION 3: Invert Binary Trees")
def invert_bt_recursive(root):
    if root is None:
        return
    
    left = invert_bt_recursive(root.left)
    right = invert_bt_recursive(root.right)
    
    root.left = right
    root.right = left
    
    return root

invert_bt_recursive(complete_tree1.root)

invert_bt_recursive(complete_tree2.root)

invert_bt_recursive(full_tree.root)

invert_bt_recursive(bin_tree.root)

    

def invert_bt_iterative(root):
    
    q = ArrayQueue()
    q.enqueue(root)
    
    while not q.is_empty():
        for _ in range(len(q)):
            node = q.dequeue()
            left = node.left
            right = node.right
            node.left = right # switch nodes
            node.right = left # switch nodes
            if left:
                q.enqueue(left)
                
            if right:
                q.enqueue(right)
        
                
    return root


invert_bt_iterative(complete_tree1.root)

invert_bt_iterative(complete_tree2.root)

invert_bt_iterative(full_tree.root)

invert_bt_iterative(bin_tree.root) 
    


#QUESTION 4
print("\n\n\nQUESTION 4: Merge Binary Trees")

def merge(t1, t2):
    if t1 and t2: #same as writing if t1 is not None and t2 is not None
        t3 = Tree.Node(t1.data + t2.data)
        t3.left = merge(t1.left, t2.left)
        t3.right = merge(t1.right, t2.right)
        return t3
        
    if t1: #and not t2; same as writing if t1 is not None and t2 is None
        t3 = Tree.Node(t1.data)
        t3.left = merge(t1.left, None)
        t3.right = merge(t1.right, None)
        return t3
        
    if t2: #and not t1; same as writing if t2 is not None and t1 is None
        t3 = Tree.Node(t2.data)
        t3.left = merge(None, t2.left)
        t3.right = merge(None, t2.right)
        return t3
        
    #not t1 and not t2; same as writing t1 is None and t2 is None
    return None


def merge_bt(root1, root2):
    root = merge(root1, root2) #you couldve just kept it as one function but this just shows that 
    return root                #merge will always return the root of two subtrees,
                               #with the main root being returned at the end of the recursive function
    

print("\nExample Tree 1:\n", bin_tree)
print("\nExample Tree 2:\n", complete_tree1)
merged_tree = LinkedBinaryTree(merge_bt(bin_tree.root, complete_tree1.root))
print("\nMerged Tree:\n", merged_tree)


    
    
