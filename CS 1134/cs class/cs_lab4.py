#Q1: palindrome checker
import math


def is_palindrome(s):
    """
    : s type: str
    : return type: bool
    """
    left = 0
    right = len(s)-1
    while left in range(len(s)):
        if s[left] != s[right]:
            return False
        left += 1
        right-= 1
    return True
print(is_palindrome('racecar'))
#compacted ver:
    #for i in range(len(s))//2)"
        #if s[i] != s[len(s)-1-i]
            #return False
        #return True

#Q2: swap vowels and return new strinc
def reverse_vowels(input_str):
    """
    : input_str type: string
    : return type: string
    """
    list_str = list(input_str) #list constructor guarantees Theta(n)
    left = 0
    right = len(list_str)-1
    while left in range(len(list_str)):
        if list_str[left] or list_str[right] == 'a' or 'e' or 'i' or 'o' or 'u':
            list_str[left], list_str[right] = list_str[right], list_str[left]
    # Your code implementation goes here
    return "".join(list_str)
print(reverse_vowels('tandon'))
#BETTER TO CONVERT TO STRING NOT LIST, vowels = 'aeiou'

#Q3: find the missing number from range(0, n)
#GIVEN example, runtime in theta(n^2)
# def find_missing(lst):
#     for num in range(len(lst) + 1):
#         if num not in lst:
#             return num

#now rewrite in runtime log(n) and consider edge cases
def find_missing(lst):
    """
    : nums type: list[int] (sorted)
    : return type: int
    """
    # question 3: part b
    # HELP HELP HELP nvm I figured it out
    #BETTER: NEED TO CHECK THE FIRST AND LAST: IF LEN = 0, OR LST[RIGHT]=RIGHT
    longest = len(lst)-1
    little = 0
    while (little <= longest):
        mid = int((little+longest)/2)
        #if first missing in the middle
        if lst[mid] != mid+1 and lst[mid-1] == mid:
            return mid+1
        #else search left
        elif lst[mid] != mid+1:
            longest = mid-1
        #else search right
        else:
            little = mid+1
        #if none missing
    return -1

#question 3: part c
#compare the sums
def find_missing_unsorted(lst):
    """
    : nums type: list[int] (unsorted)
    : return type: int
    """
    temp_sum = 0
    left = 0
    right = len(lst) - 1
    mid = int(math.floor(left + right) / 2)
    while (left <= right):
        # the middle element is missing
        if mid*2 != sum(lst[left]+lst[right])-1 or sum(lst[left]+lst[right])+1:
            return lst[mid]
        # any element is missing
        if lst[left] + lst[right] != lst[left + 1] + lst[right - 1]:
            if lst[left]+1 != lst[left+1] and lst[right]-1 == lst[right-1]:
                return lst[left]
            return lst[right]
        left += 1
        right -= 1
    # no element is missing
    return 'nothing is missing'

#BETTER PART C:
# n = len(lst)
# expected = n*(n+1) //2
# actual = sum(lst)
# missing num = expected - actual
# return missing
#ALTERNATIVE: NEW LIST AND PUT NUMBERS, FIND NULL VALUE
#OH IT HAS TO RUN IN THETA(N)

lst = [0, 1, 2, 3, 4, 5, 6, 8] #seven is missing
#the function should return num


#Q4: find the pivot of a sorted list by random k steps... left? right? what is this
#PART A: TIME in O(LOG(N))
def find_pivot(lst):
    l = 0
    r = len(lst) - 1
    mid = l

    while l < r:
        mid = (l+r) //2
        if (lst[mid] > lst[right]):
            l = mid +1
        else:
            r = mid
    return l

#Q4: PART B: FIND THE TARGET VALUE
#BIGGER, FIND PIVOT, RETURN INT
