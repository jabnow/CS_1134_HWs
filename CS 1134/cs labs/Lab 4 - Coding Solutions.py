"""
1134 Lab 4 - Coding Solutions
Spring 2024
"""

# 1
"""
2 pointers - moving inwards
Compare letters at both pointers, if they match continue moving inwards.
Otherwise, no longer a palindrome and return False.
"""
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# compacted by calculating pointer using other pointer
def is_palindrome2(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1 - i]: #or s[-1 - i]
            return False
    return True



# 2
"""
2 pointers - 2 pointers moving inwards
Very similar to the is_palindrome question. The only difference is that we need to check if the letters are vowels.
If both are vowels, swap them. Otherwise, if not a vowel, move the pointer inwards.
"""
def reverse_vowels(input_str):
    left = 0
    right = len(input_str) - 1
    vowels = 'aeiou'
    lst = list(input_str) # convert string to list - linear operation
    
    while left < right: # can't use for loop because you don't know where vowels are placed
        if lst[left] in vowels and lst[right] in vowels:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

        # Note: 2 separate if statements instead of elif because we want to move both pointers
        # inwards if both letters are not vowels
        if lst[left] not in vowels:
            left += 1

        if lst[right] not in vowels:
            right -= 1

    return "".join(lst) # join list into single string - linear operation


# 3
# 3.a
"""
O(n^2) runtime due to use of 'in' operator. 'in' does a linear search through the list to find the element.
Thus, the runtime is O(n) and we are doing this n times, so O(n^2).
"""

# 3.b
def find_missingb(lst):
    """
    The key idea is that the missing value is the first index i where
    lst[i] != i. We will binary search for this index.

    Furthermore, if lst[i] != i, then lst[j] != j for all j > i.
    i.e. once the index and the value don't correspond, they will never correspond again

    (If you are not convinced of this fact, try some examples)

    Thus, if we check whether middle value has this property, we can adjust the range accordingly.
    """
    left = 0
    right = len(lst) - 1

    # Edge cases: first num missing
    if len(lst) == 0:
        return 0
    # last num missing
    if lst[right] == right: #if lst[right] == right, there is no index where lst[i] != i. Thus, the missing value is the length of the list itself
        return len(lst)

    while left < right:
        mid = (left + right) // 2 # get middle index
        if lst[mid] != mid:
            right = mid
            """
            Note that we need to keep recursing. If lst[mid] = mid, we don't know for sure if mid is the first index
            where this is not true. We just know that the first one must be to the left of mid.
            """
        else:
            left = mid + 1
            """
            mid is for sure not the index we are looking for, so left becomes mid + 1, not just mid.
            We always want to be searching a valid range
            """

    return left # or right, as when the loop breaks, left == right (because we are always searching a valid range)

# 3.c
def find_missingc(lst):
    """
    If all the numbers between 0 and n were present, the sum of the elements of the list would be
    0 + 1 + 2 + 3 + .... + n = n(n+1)/2

    But, somewhere, an element (i) is missing. The sum of the list is thus
    0 + 1 + 2 + 3 + ... + (i - 1) + (i + 1) + ... + n

    If we subtract these two quantities, we find the missing number i.
    """
    n = len(lst)

    expected_sum = n*(n+1)//2
    actual_sum   = sum(lst)
    missing_num  = expected_sum - actual_sum

    return missing_num


# Q4 Part A
def find_pivot(lst):
    left = 0
    right = len(lst) - 1
    mid = left

    while left < right:
        mid = (left + right)//2

        if (lst[mid] > lst[right]): #if the right bound is smaller than the mid, this part is not sorted
            left = mid + 1 #only increment left, because the smallest should be on the left side
        else: #lst[mid] < lst[left] left bound biger than mid, this part is not sorted
            right = mid
    return left


# Q4 Part B
def shift_binary_search(lst, target):
    mid = find_pivot(lst) #save the pivot
    left = 0
    right = len(lst) - 1
#ex) [left ... mid] [mid ... right] pivot is the mid; find out which part of the list to search in
    
    if lst[mid] <= target <= lst[right]: #if in [mid ... right] --> left is mid
        left = mid
    
    else: #else in [left ... mid] --> right is mid
        right = mid
    #now binary search
    while left <= right:
        mid = (left + right) //2
        
        if lst[mid] == target:
            return mid

        elif lst[mid] < target:
            left = mid + 1

        else: #lst[mid] > target
            right = mid - 1

    return None #couldn't find


# 5a
import math

def jump_search_k(lst, val, k):

    if len(lst) == 0: #check if list not empty first
        return None
    
    curr = 0
    prev = curr #save the prev jump point
    jump = k #how much you jump, this is your k

    #jump not out of bound and lst[curr] < val
    while curr < len(lst) and lst[curr] < val:
        prev = curr
        curr += jump
    #if jump out of range for a non perfect square size
    if curr >= len(lst):
        prev = curr - jump #jump back to prev
        curr = len(lst) - 1 #change upper bound to last index
    #linear search back at most n//k values
    while curr >= prev:
        if lst[curr] == val:
            return curr
        curr -= 1
    return None #couldn't find it


# 5b
def jump_search(lst, val):
    if len(lst) == 0: #check if list not empty first
        return None
    
    curr = 0
    prev = curr #save the prev jump point
    jump = math.floor(math.sqrt(len(lst))) #how much you jump, this is your k
    #int( len(lst) ** (0.5) )
    #jump not out of bound and lst[curr] < val
    while curr < len(lst) and lst[curr] < val:
        prev = curr
        curr += jump

    #if jump out of range for a non perfect square size
    if curr >= len(lst):
        prev = curr - jump
        curr = len(lst) - 1 #change upper bound to last index

    #linear search back at most sqrt(n) values, k == sqrt(n)
    while curr >= prev:
        if lst[curr] == val:
            return curr
        curr -= 1
    return None #couldn't find it
    
    
'''
lst = [-1111, -818, -646, -50, -25, -3, 0, 1, 2, 11, 33, 45, 46, 51, 58, 72, 74, 75, 99, 110, 120, 121, 345, 400, 500, 999, 1000, 1114, 1134, 10010, 500000, 999999]
#Testing k
for i in range(1, len(lst)):
# print("i:",i)
print("TESTING VALUES IN LIST:", "k = ", i, "\n")
for val in lst:
if jump_search_k(lst, val, i) is None:
print(val, "FAILED - DID NOT FIND")
#just to make sure you’re not stuck in an infinite loop print("TEST k COMPLETED")
#Testing sqrt

 print("\nTESTING VALUES IN LIST: k = sqrt(n) \n")
for val in lst:
if jump_search(lst, val) is None:
print(val, "FAILED - DID NOT FIND")
#just to make sure you’re not stuck in an infinite loop print("TEST sqrt COMPLETED")
'''


# 6
def exponential_search(lst, val):

    if len(lst) == 0: #check if list is not empty
        return None
    
    if lst[0] == val: #check index 0 first
        return 0
    else:
        i = 1 #start at 1 for the exponential search
    while i * 2 < len(lst) and lst[i] < val:
        i *= 2
    left = i//2
    right = i
    if lst[right] < val: #check if out of bounds (exited because i * 2 < len(lst))
        right = len(lst) - 1
    
    #now binary search
    while left <= right:
        mid = (left + right)//2
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            left = mid + 1
        elif lst[mid] > val:
            right = mid - 1

    return None
    
#testing exponential search
lst = [-1111, -818, -646, -50, -25, -3, 0, 1, 2, 11, 33, 45, 46, 51, 58, 72, 74, 75, 99, 110, 120, 121, 345, 400, 500, 999, 1000, 1114, 1134, 10010, 500000, 999999]
'''
print("TESTING VALUES IN LIST:\n")
for val in lst:
if exponential_search(lst, val) is None:
print(val, "FAILED - DID NOT FIND")
#just to make sure you’re not stuck in an infinite loop print("TEST COMPLETED")
'''

lst = [2,3,4,1]
print(shift_binary_search(lst, 1))
