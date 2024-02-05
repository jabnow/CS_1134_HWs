def shift(lst, k, direction='left'):
    lst2 = [0]*len(lst)
    if direction == "right":
        #mutate list to shift to right
        for i in range(0, len(lst), 1):
            lst2[i] = lst[i-k]
        for i in range(len(lst)-1, -1, -1):
            lst[i] = lst2[i]
    else:
        #direction == null or 'left'
        for i in range(len(lst)-1, -1, -1):
        #just assign values to lst2
            lst2[i] = lst[i-k]
        for i in range(0, len(lst)):
        #assign val in lst2 to lst
            lst[i] = lst2[i]
    return lst


# def shift(lst, k):
#     #given list of N items, k < N
#     for i in range(0, k):
#         lst.append(lst[i])
#     for i in range(0, k):
#         lst.remove(lst[i-1])
#     return lst
#this is probably illegal?
