# QUESTION 4
def list_min(lst, low, high):
    # if the list is 1 element
    # create a variable for current min value
    # if the lst[low] < min value
    # recursive step
    # do it for left and right sides --> better runtime
    if low >= high:
        return lst[low]
    mid = (low + high) // 2
    left_min = list_min(lst, low, mid)
    right_min = list_min(lst, mid+1, high)
    if left_min > right_min:
        return right_min
    else:
        return left_min

def list_min_2(lst, low, high):
    if low == high:
        return lst[low]
    suspect = list_min_2(lst, low+1, high)
    if suspect >= lst[low]:
        suspect = lst[low]
    return suspect