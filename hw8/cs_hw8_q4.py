from BinarySearchTreeMap import BinarySearchTreeMap


def find_min_abs_difference(bst):
    def helper(node):
        if node is None:
            return []
        return helper(node.left) + [node.item.key] + helper(node.right)

    nodes_list = helper(bst.root)
    if len(nodes_list) < 2:
        return None  # Handle edge case when there are less than 2 nodes

    orig_min = abs(nodes_list[0] - nodes_list[1])

    for i in range(1, len(nodes_list) - 1):
        new_min = abs(nodes_list[i + 1] - nodes_list[i])
        if new_min < orig_min:
            orig_min = new_min
    return orig_min



"""When called, it returns the minimum absolute difference between keys of any two
nodes in bst.
    The runtime of this function should be linear. That
is, if bst contains n nodes, this function should run in Θ(n).
Hint: To meet the runtime requirement, you may want to define an additional,
recursive, helper function, that returns more than one value (multiple return values
would be collected as a tuple)."""
