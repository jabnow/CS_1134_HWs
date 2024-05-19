from LinkedBinaryTree import LinkedBinaryTree

# question 5 part a
""" The function is given a string prefix_exp_str, which contains an arithmetic
expression in a prefix notation.
When called, it creates and returns a LinkedBinaryTree object, that is the
expression tree representing prefix_exp_str.

    Assume that prefix expression will come in the following format:
1. All operators in the expression will be taken from the four basic arithmetic
operations (+, -, * and /).
2. All operands will be positive integers.
3. The tokens in the expression will be separated by a space.

    Implementation requirements:
1. The nodes containing operators, should have the operator as a string, and
nodes containing numerals, should have the number as an int.
2. The runtime for creating the expression tree should be linear.
3. You are not allowed to use a stack in your implementation.
    """

def create_expression_tree(prefix_exp_str):
    def create_expression_tree_helper(prefix_exp_str, start_pos):
        pointer = prefix_exp_str[start_pos]
        if pointer not in "+-/*":  # then it's an int
            root = LinkedBinaryTree.Node(int(pointer))
            # return (subtree created, subtree size)
            return (root, start_pos + 1)
        left_val = create_expression_tree_helper(prefix_exp_str, start_pos + 1)
        right_val = create_expression_tree_helper(prefix_exp_str, left_val[1])
        root = LinkedBinaryTree.Node(pointer, left_val[0], right_val[0])
        return (root, right_val[1])

    lst_str = prefix_exp_str.split()
    return LinkedBinaryTree(create_expression_tree_helper(lst_str, 0)[0])


# question 5 part b

def prefix_to_postfix(prefix_exp_str):
    bin_tree = create_expression_tree(prefix_exp_str)
    postfix_lst = []
    for node in bin_tree.postorder():
        postfix_lst.append(str(node.data))  # is .join() linear??
    return " ".join(postfix_lst)


"""
Hint: There is more than one way to solve this problem. One way is to start by
creating a list with the expression’s tokens (by using the split method), and then
calling a helper function:
"""
