from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        """ Initializes an Integer object representing
                the value given in the string num_str"""
        self.data = DoublyLinkedList()
        for i in range(len(num_str)):
            self.data.add_last(int(num_str[i]))
        # remove any leading zeroes
        while self.data.header.next.data == 0 and len(self.data) > 1:
            self.data.delete_first()

    def __add__(self, other):
        """ Creates and returns an Integer object that
                represent the sum of self and other, also of
                type Integer"""
        num_res = Integer("")
        pointer1 = self.data.trailer.prev
        pointer2 = other.data.trailer.prev
        extra = 0

        while (pointer1.data and pointer2.data) is not None:
            result = pointer1.data + pointer2.data + extra
            num_res.data.add_first(result % 10)  # from ones position onwards
            extra = result // 10  # if necessary
            # update the pointers
            pointer1 = pointer1.prev
            pointer2 = pointer2.prev
        # end means one is None
        if pointer1.data is not None:
            longer = pointer1
        else:
            longer = pointer2

        while longer.data is not None:
            result = longer.data + extra
            num_res.data.add_first(result % 10)
            extra = result // 10
            longer = longer.prev
        # finally
        if extra != 0:
            num_res.data.add_first(extra)
        return num_res

    def __repr__(self):
        """ Creates and returns the string representation
                of self"""
        num_str = ""
        pointer = self.data.header.next
        while pointer.data is not None:
            num_str += str(pointer.data)
            pointer = pointer.next
        return num_str

    def __mul__(self, other):  # optional, do last
        """ Creates and returns an Integer object that
                represent the multiplication of self and other,
                also of type Integer"""
        pointer1 = self.data.trailer.prev
        product = Integer("")

        for i in range(len(self.data)):
            extra = 0
            pointer2 = other.data.trailer.prev
            temp_res = Integer("")
            # for each digit of self, match with other
            for j in range(len(other.data)):
                result = pointer1.data * pointer2.data + extra
                temp_res.data.add_first(result % 10)
                extra = result // 10
                pointer2 = pointer2.prev
            # after all mult
            if extra != 0:
                temp_res.data.add_first(extra)
            # any 0s
            for j in range(i):
                temp_res.data.add_last(0)
            product = product + temp_res
            pointer1 = pointer1.prev
            # rid extra 0s
            while product.data.header.next.data == 0 and len(product.data) > 1:
                product.data.delete_first()
            return product
