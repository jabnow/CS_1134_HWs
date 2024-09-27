def shift(lst, k, direction='left'):
    if direction == 'left':
        lst2 = [0] * len(lst)
        for i in range(len(lst) - 1, -1, -1):
        #just assign values to lst2
            lst2[i-k] = lst[i]
        for i in range(len(lst)):
        #assign values in lst2 to lst
            lst[i] = lst2[i]
        return lst
    elif direction == 'right':
        lst2 = []
        #the elements that rotate to the front
        for i in range(len(lst)-k, len(lst)):
            lst2.append(lst[i])
        #the other elements are displaced
        for i in range(0, len(lst)-k):
            lst2.append(lst[i])
        #reassign to original list
        for i in range(0, len(lst)):
            lst[i] = lst2[i]
        return lst

