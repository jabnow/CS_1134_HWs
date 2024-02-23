#Q3
import math
def factors(num):
    """
    returns a sorted generator with runtime theta(sqrt(n))
    """
    #needs to find the factors for any number
    #maybe only needs to run halfway and compute the larger factors
    #array, two indeces, or k slices and store into new array
    i = 1
    for i in range(i,num+1):
        if not num%i:
            yield i

for curr_factor in factors(100):
    print(curr_factor, end=' ')
    #1 2 4 5 20 25 50 100

#Q4: e approximation
def e_approx(n):
    """
    returns an approximation of e,
    calculated by the sum of the first (n+1)
    e = 1 + 1/i! ...1/(n+1)!
    should run in theta(n)
    """
    curr_sum = 1
    curr_product = 1
    i = 1
    while i <= n:
        curr_product *= i
        curr_sum += 1 / curr_product
        i += 1
    return curr_sum
def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)


#Q5
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

#Q6
def two_sum(srt_lst, target):
    """
    returns two indices in a tuple: ()
    so that the elements add up to the target
    otherwise return None
    """
    #should have a linear run time
    #what if there are multiple combos
    #move one side, calculate the diff, search for it on the other side
    mid = len(srt_lst)//2
    temp = 0
    right = len(srt_lst)
    for i in range(mid):
        temp = target - srt_lst[i]
        for j in range(mid, right):
            if srt_lst[j] == temp:
                return (i, j)
    return None

    #TRY 2
    l, r = 0, len(srt_lst)-1
    while l < r:
        sumd = srt_lst[l] + srt_lst[r]
        if sumd == target:
            return (l,r)
        elif sumd > target:
            r -= 1
        else:
            l += 1
    return None


srt_lst = [-2, 7, 11, 15, 20, 21]
target = 22
print(two_sum(srt_lst, target))
#function returns (1,3) for srt_lst[1]+srt_lst[3]= 7+15= 22

#Q7
def findChange(lst01):
    """
    list of 0s and 1s. Returns the index of the first 1.
    """
    #runtime should be theta(log(n))
    l = 0
    r = len(lst01)-1
    while l < r:
        mid = (l+r) // 2
        if lst01[mid] == 0:
            l = mid+1
        else:
            r = mid
    return l


lst01 = [0, 0, 0, 0, 0, 1, 1, 1]
print(findChange(lst01))
#should return 5
