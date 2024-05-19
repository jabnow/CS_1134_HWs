from LinkedBinaryTree import LinkedBinaryTree

# question 3

def is_height_balanced(bin_tree):
    """ the height of a subtree rooted at r will
be the number of nodes on such a longest path. By this definition, a leaf node has height 1,
while we trivially define the height of a “None” child to be 0.
    Given bin_tree, a LinkedBinaryTree object, it will return True if the tree
satisfies the height-balance property, or False otherwise.
    Implementation requirement: Your function should run in linear time.
    To meet the runtime requirement, you may want to define an additional,
recursive, helper function, that returns more than one value (multiple return values
could be collected as a tuple).
    """
    def balance_subtree(root):
        if root is None:
            return (0, True)
        left_val = balance_subtree(root.left)
        right_val = balance_subtree(root.right)
        height_val = max(left_val[0], right_val[0]) + 1

        if abs(left_val[0] - right_val[0]) > 1 or (left_val[1] and right_val[1]) is not True:
            return (height_val, False)
        else:
            return (height_val, True)

    if bin_tree is None:
        raise Exception("Tree does not exist, neither does height")
    else:
        return balance_subtree(bin_tree.root)[1]
