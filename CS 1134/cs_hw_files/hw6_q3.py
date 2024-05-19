from DoublyLinkedList import DoublyLinkedList


class CompactString:
    """
    We will represent such strings as a linked list, where each maximal sequence of the
same character in consecutive positions, will be stored as a single tuple containing
the character and its count.
    """

    def __init__(self, orig_str):
        """ Initializes a CompactString object
    representing the string given in orig_str"""
        self.data = DoublyLinkedList()
        occur = 1
        for i in range(1, len(orig_str)):
            if orig_str[i] == orig_str[i-1]:
                occur += 1
            else:
                self.data.add_last((orig_str[i-1], occur))
                occur = 1
        if len(orig_str) != 0:
            self.data.add_last((orig_str[len(orig_str)-1], occur))

    def __add__(self, other):
        """ Creates and returns a CompactString object that
    represent the concatenation of self and other,
    also of type CompactString"""
        new_comp = CompactString("")
        pointer = self.data.header.next
        alt_pointer = other.data.header.next

        while pointer.data is not None:
            new_comp.data.add_last(pointer.data)
            pointer = pointer.next

        while alt_pointer.data is not None:
            new_comp.data.add_last(alt_pointer.data)
            alt_pointer = alt_pointer.next

        return new_comp

    def __lt__(self, other):
        """ returns True if self is lexicographically
    less than other, also of type CompactString"""
        pointer1 = self.data.header.next
        pointer2 = other.data.header.next

        while pointer1.data == pointer2.data and pointer1.data is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        if pointer1.data is None and pointer2.data is not None:
            return True
        elif pointer2.data is None and pointer1.data is not None:
            return False
        elif pointer1.data is None and pointer2.data is None:
            return False

        else:
            if pointer1.data[0] == pointer2.data[0]:
                if pointer1.data[1] > pointer2.data[1]:
                    if pointer2.next.data is None:
                        return False
                    return pointer1.data[0] < pointer2.next.data[0]
                else:
                    if pointer1.next.data is None:
                        return True
                    return pointer1.next.data[0] < pointer2.data[0]
            return pointer1.data[0] < pointer2.data[0]

    def __le__(self, other):
        """ returns True if self is lexicographically
    less than or equal to other, also of type
    CompactString"""
        pointer1 = self.data.header.next
        pointer2 = other.data.header.next

        while pointer1.data == pointer2.data and pointer1.data is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        if pointer1.data is None and pointer2.data is not None:
            return False
        elif pointer2.data is None and pointer1.data is not None:
            return True
        elif pointer1.data is None and pointer2.data is None:
            return True

        else:
            if pointer1.data[0] == pointer2.data[0]:
                if pointer1.data[1] >= pointer2.data[1]:
                    if pointer2.next.data is None:
                        return False
                    return pointer1.data[0] <= pointer2.next.data[0]
                else:
                    if pointer1.next.data is None:
                        return True
                    return pointer1.next.data[0] <= pointer2.data[0]
            return pointer1.data[0] <= pointer2.data[0]

    def __gt__(self, other):
        """ returns True if self is lexicographically
    greater than other, also of type CompactString"""
        pointer1 = self.data.header.next
        pointer2 = other.data.header.next

        while pointer1.data == pointer2.data and pointer1.data is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        if pointer1.data is None and pointer2.data is not None:
            return False
        elif pointer2.data is None and pointer1.data is not None:
            return True
        elif pointer1.data is None and pointer2.data is None:
            return False

        else:
            if pointer1.data[0] == pointer2.data[0]:
                if pointer1.data[1] > pointer2.data[1]:
                    if pointer2.next.data is None:
                        return True
                    return pointer1.data[0] > pointer2.next.data[0]
                else:
                    if pointer1.next.data is None:
                        return False
                    return pointer1.next.data[0] > pointer2.data[0]
            return pointer1.data[0] > pointer2.data[0]

    def __ge__(self, other):
        """ returns True if self is lexicographically
    greater than or equal to other, also of type
    CompactString"""
        pointer1 = self.data.header.next
        pointer2 = other.data.header.next

        while pointer1.data == pointer2.data and pointer1.data is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        if pointer1.data is None and pointer2.data is not None:
            return False
        elif pointer2.data is None and pointer1.data is not None:
            return True
        elif pointer1.data is None and pointer2.data is None:
            return True

        else:
            if pointer1.data[0] == pointer2.data[0]:
                if pointer1.data[1] >= pointer2.data[1]:
                    if pointer2.next.data is None:
                        return True
                    return pointer1.data[0] >= pointer2.next.data[0]
                else:
                    if pointer1.next.data is None:
                        return False
                    return pointer1.next.data[0] >= pointer2.data[0]
            return pointer1.data[0] >= pointer2.data[0]

    def __repr__(self):
        """ Creates and returns the string representation
    (of type str) of self"""
        res_str = ""
        pointer = self.data.header.next
        while pointer.data is not None:
            res_str += pointer.data[0] * pointer.data[1]
            pointer = pointer.next
        return res_str
