from BinarySearchTreeMap import BinarySearchTreeMap


def restore_bst(prefix_lst):
    def restore_helper(prefix_lst, min_val, max_val, index):
        if index >= len(prefix_lst):
            return None, index

        if min_val < prefix_lst[index] < max_val:
            item = BinarySearchTreeMap.Item(prefix_lst[index])
            node = BinarySearchTreeMap.Node(item)

            left, index = restore_helper(prefix_lst, min_val, item.key, index + 1)
            right, index = restore_helper(prefix_lst, item.key, max_val, index)

            node.left = left
            node.right = right

            if left:
                left.parent = node
            if right:
                right.parent = node

            return node, index

        return None, index

    bst = BinarySearchTreeMap()
    if prefix_lst:
        root, value = restore_helper(prefix_lst, float('-inf'), float('inf'), 0)
        bst.root = root
        bst.n = len(prefix_lst)
    return bst

"""
    1. The runtime of this function should be linear.
2. Assume that prefix_lst contains integers.
3. Assume that there are no duplicate values in prefix_lst.
4. You may want to define a helper function.
"""

