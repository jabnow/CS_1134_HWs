from BinarySearchTreeMap import BinarySearchTreeMap

# part a
def create_chain_bst(n):
    chain_bst = BinarySearchTreeMap()
    for num in range(n):
        chain_bst.insert(num+1, None)
    return chain_bst


# given
def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst


# part b
def add_items(bst, low, high):
    mid = (low + high) // 2
    bst.insert(mid, None)
    if low != high:
        add_items(bst, low, mid - 1)
        add_items(bst, mid + 1, high)


# part c
"""I FORGOT TO DO THE RUNTIME ANALYSIS ON PAPER
PART a -- create chain runs in O(h = n) since just adding
          create complete_bst runs in theta(logn) due to recursion
PART b -- runs in O(logn) since nothing repeats"""