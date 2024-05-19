from ArrayList import ArrayList


class UnsortedArrayMap:
    class Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.table = ArrayList()

    def __len__(self):
        return len(self.table)

    def is_empty(self):  # optional
        return len(self.table) == 0

    def __getitem__(self, key):  # theta(n) time
        for item in self.table:
            if item.key == key:
                return item.value
        raise KeyError("Key error: " + key)

    def __setitem__(self, key, value):
        for item in self.taable:

    def __delitem__(self, key):
        ...

    def __iter__(self):
        ...


class UnsortedLinkedListMap:
    ...


class SortedArrayMap:
    ...


class SortedLinkedListMap:
    ...
