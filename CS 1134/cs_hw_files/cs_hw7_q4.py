from ArrayQueue import ArrayQueue
#from ArrayStack import ArrayStack


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self
            self.parent = None

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return left_count + right_count + 1

        return subtree_count(self.root)

    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return left_sum + right_sum + root.data

        return subtree_sum(self.root)

    def height(self):
        def subtree_height(root):
            if ((root.left is None) and (root.right is None)):
                return 0
            elif (root.right is None):  # left is not None
                left_height = subtree_height(root.left)
                return 1 + left_height
            elif (root.left is None):  # right is not None
                right_height = subtree_height(root.right)
                return 1 + right_height
            else:  # both subtrees are not None
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if (self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)

    def preorder(self):
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)

    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)

    def breadth_first(self):
        if (self.is_empty()):
            return
        bfs_queue = ArrayQueue()
        bfs_queue.enqueue(self.root)
        while (bfs_queue.is_empty() == False):
            curr_node = bfs_queue.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                bfs_queue.enqueue(curr_node.left)
            if (curr_node.right is not None):
                bfs_queue.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.inorder():
            yield node.data

    def preorder_with_stack(self):
        ''' Returns a generator function that iterates through
        the tree using the preorder traversal '''
        stack = ArrayStack()
        stack.push(self.root)
        while (len(stack) > 0):
            node = stack.pop()
            if (node.right is not None):
                stack.push(node.right)
            if (node.left is not None):
                stack.push(node.left)
            yield node.data

    def eval_exp_tree(exp_t):
        def subtree_eval_exp(root):
            if ((root.left is None) and (root.right is None)):
                return root.data
            else:
                left_arg = subtree_eval_exp(root.left)
                right_arg = subtree_eval_exp(root.right)
                if (root.data == "+"):
                    return left_arg + right_arg
                elif (root.data == "-"):
                    return left_arg - right_arg
                if (root.data == "*"):
                    return left_arg * right_arg
                if (root.data == "/"):
                    return left_arg / right_arg

        return subtree_eval_exp(exp_t.root)

# question 4 (OPTIONAL)

    def iterative_inorder(self):
        """ When called on a tree, it will create a generator, allowing to iterate over the values
    of the tree in an in-order order.
        Implementation requirements:
        1. You should make a purely iterative implementation. Recursion is not allowed.
        2. Your method is not allowed to call any helper methods or functions. All the
    work should be done inside this method.
        3. In addition to the tree, you may use only theta(1) additional memory. That is, you
    are not allowed to use any additional data structure (such as stack, queue, list,
    etc.).
        4. The total runtime to iterate over an entire tree should be linear.
    Note: When you will be done with this question, you will truly appreciate the
    simplicity and elegance of recursion >:)
        """
        curr_node = self.root
        while curr_node is not None:  # left, root, right
            if curr_node.left is None:
                pointer = None
                while curr_node is not None and (curr_node.right is None or curr_node.right is pointer):
                    pointer = curr_node
                    if curr_node.right is None:
                        yield curr_node.data
                    curr_node = curr_node.parent
                if curr_node is not None:
                    yield curr_node.data
                    curr_node = curr_node.right
            else:
                curr_node = curr_node.left


    """
    For example, if t is the tree from question 1, when running the following code:
    for item in t.iterative_inorder():
    print(item, end=' ')
    print()
    You should expect the following output:
    5 9 1 2 3 8 7 4
    """
