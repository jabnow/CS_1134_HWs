def split_parity(lst):
    """
    orders a list of integers for odds first, evens last
    inner order doesn't matter
    cannot use a temp local list, runtime should be theta(n)
    """
    n = len(lst)
    low = 0
    i = 0
    #found an odd
    while i < n:
        if lst[i]%2 != 0:
            lst[i], lst[low] = lst[low], lst[i]
            low += 1
        i += 1
    return lst

def main():
    lst = [1,2,3,4]
    print(split_parity(lst))
