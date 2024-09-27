from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    """srt_lnk_lst2. The elements in srt_lnk_lst1 and srt_lnk_lst2 are sorted.
    create and return a new doubly linked list that
contains all the elements that appear in the input lists in a sorted order.

if srt_lnk_lst1= [1 <--> 3 <--> 5 <--> 6 <--> 8],
and srt_lnk_lst2=[2 <--> 3 <--> 5 <--> 10 <--> 15 <--> 18],
calling: merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2), should
create and return a doubly linked list that contains:
[1 <--> 2 <--> 3 <--> 3 <--> 5 <--> 5 <--> 6 <--> 8 <--> 10 <--> 15 <--> 18]."""

    def merge_sublist(node1, node2, srt_lnk_lst1, srt_lnk_lst2):
        new_lst = DoublyLinkedList()
        if node1.data is None and node2.data is not None:
            while node2.data is not None:
                new_lst.add_last(node2.data)
                node2 = node2.next
        elif node2.data is None and node1.data is not None:
            while node1.data is not None:
                new_lst.add_last(node1.data)
                node1 = node1.next
        else:
            if node1.data <= node2.data:
                new_lst = merge_sublist(node1.next, node2, srt_lnk_lst1, srt_lnk_lst2)
                new_lst.add_first(node1.data)
            else:
                new_lst = merge_sublist(node1, node2.next, srt_lnk_lst1, srt_lnk_lst2)
                new_lst.add_first(node2.data)
        return new_lst

    return merge_sublist(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next, srt_lnk_lst1, srt_lnk_lst2)



"""
NOTES

1. You need to decide on the signature of merge_sublists.
2. merge_sublists has to be recursive.
3. An efficient implementation of merge_sublists would allow
merge_linked_lists to run in linear time. That is, if n1 and n2 are the sizes
of the input lists, the runtime would be theta(n1 + n2).
"""


"""
ERROR
Test Failed: 'Node' object has no attribute 'header'
"""