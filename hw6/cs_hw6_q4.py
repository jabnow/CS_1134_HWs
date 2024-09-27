from DoublyLinkedList import DoublyLinkedList


def copy_linked_list(lnk_lst):
    """The function is given a nested doubly linked lists of integers lnk_lst, and
returns a shallow copy of lnk_lst.
    Note: lnk_lst could have multiple levels of nesting."""
    lst_copy = DoublyLinkedList()
    for elem in lnk_lst:
        lst_copy.add_last(elem)
    return lst_copy


def deep_copy_linked_list(lnk_lst):
    """The function is given a nested doubly linked lists of integers lnk_lst, and
returns a deep copy of lnk_lst.
    Note: lnk_lst could have multiple levels of nesting."""
    deep_lst = DoublyLinkedList()
    for elem in lnk_lst:
        if isinstance(elem, int):
            deep_lst.add_last(elem)
        else:
            deep_lst.add_last(deep_copy_linked_list(elem))
    return deep_lst

