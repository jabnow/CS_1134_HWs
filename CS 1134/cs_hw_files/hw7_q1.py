from LinkedBinaryTree import LinkedBinaryTree

# question 1

def min_and_max(bin_tree):
    """ When called on a LinkedBinaryTree, containing numerical data in all its nodes,
it will return a tuple, containing the maximum and minimum values in the tree.
For example, given the following tree:
    1. Define one additional, recursive, helper function:
def subtree_min_and_max(root)
That is given root, a reference to a node in a LinkedBinaryTree tree. When
called, it should return the minimum and maximum tuple for the subtree rooted
by root.
    2. In your implementations, you are not allowed to use any method from the
LinkedBinaryTree class. Specifically, you are not allowed to iterate over the
tree, using any of the traversals.
    3. Your function should run in linear time.
    4. Since the maximum and minimum are not defined on an empty set of elements, if
the function is called on an empty tree you should raise an exception.
    """

    def subtree_min_and_max(root):
        if root is None:
            raise AttributeError("bin_tree empty, no min / max")

        if root.left is None and root.right is None:
            return (root.data, root.data)  # min, max

        elif root.left is None and root.right is not None:
            right_val = subtree_min_and_max(root.right)
            return (min(root.data, right_val[0]), max(root.data, right_val[1]))

        elif root.right is None and root.left is not None:
            left_val = subtree_min_and_max(root.left)
            return (min(root.data, left_val[0]), max(root.data, left_val[1]))

        else:
            left_val = subtree_min_and_max(root.left)
            right_val = subtree_min_and_max(root.right)

            min_val = min(left_val[0], root.data, right_val[0])
            max_val = max(left_val[1], root.data, right_val[1])

            return (min_val, max_val)

    return subtree_min_and_max(bin_tree.root)

