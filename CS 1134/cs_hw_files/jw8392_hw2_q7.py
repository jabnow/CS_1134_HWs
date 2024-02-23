def findChange(lst01):
    """
    list of 0s and 1s. Returns the index of the first 1.
    runtime should be theta(log(n))
    """
    l = 0
    r = len(lst01)-1
    while l < r:
        mid = (l+r) // 2
        if lst01[mid] == 0:
            l = mid+1
        else:
            r = mid
    return l

def main():
    lst01 = [0, 0, 0, 0, 0, 1, 1, 1]
    print(findChange(lst01))