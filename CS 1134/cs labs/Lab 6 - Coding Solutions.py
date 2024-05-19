# QUESTION 1
# Write a recursive function that returns the sum of all numbers from 0 to n. (5 minutes)
def sum_to(n):
    if n < 0:
        return 0
    return n + sum_to(n-1)


# QUESTION 2
# Write a recursive function that returns the product
    # of all even numbers from 1 to n.
def product_evens(n):
    if n == 1:
        return 1
    if n % 2 == 0: # is even
        return n * product_evens(n-1) # or you can just do product_evens(n-2) because,
                                        # even - 2 is always even so you'll never get odd
    else:
        return product_evens(n-1)


# QUESTION 3
# Write a recursive function to find the maximum element in a non-empty, non-sorted list of numbers.
def find_max(lst, low, high):
    if low == high:
        return lst[low] # the base case will be the default max
    curr_max = find_max(lst, low + 1, high) # the idea is to get the curr max from the next recursive call
    if lst[low] > curr_max:
        curr_max = lst[low]
    return curr_max


# QUESTION 4
# Write a recursive function to determine if a string is a palindrome.
def is_palindrome(str, low, high):
    if low >= high:
        return True
    elif str[low] != str[high]:
        return False
    return is_palindrome(str, low+1, high-1)
# alternatively
# return str[low] == str[high] and is_palindrome(str, low+1, high-1)


# QUESTION 5
# Give a recursive implementation for the binary search algorithm.
''' Given the binary search with while loop
while low <= high: # exit if low > high
    mid = (low + high)//2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
return None
'''

def binary_search(nums, target, low, high):
    if low > high: # exit condition
        return None
    mid = (low + high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, target, mid+1, high) # low = mid + 1
    else: # nums[mid] > target
        return binary_search(nums, target, low, mid-1) # high = mid - 1


# QUESTION 6
# Given a string of letters representing a word(s), write a recursive function that returns
# a tuple of 2 integers: the number of vowels, and the number of consonants in the word.
def vc_count(word, low, high):
    if low >= high:
        if word[low] in "aeiouAEIOU": # base case, starting tuple
            return (1,0) # (1 vowel, 0 consonants)
        return (0,1) # else (0 vowels, 1 consonant)
    else:
        prev = vc_count(word, low+1, high) # get the tuple from the next recursive call
        if word[low] in "aeiouAEIOU":
            return (prev[0] + 1, prev[1]) # update it
        return (prev[0], prev[1] + 1)


# QUESTION 7
# Given a list of integers, write a function to print the sum triangle of the array.
def list_sum_triangle(lst):
    if len(lst) >= 1:
        temp = lst.copy() # make a copy for printing the current list
        # for i in range(len(lst)-1): # same thing as the sum_row
        # lst[i] += lst[i+1]
        sum_row(lst, 0, len(lst)-1) # modify the list
        lst.pop() # get rid of the last element
        list_sum_triangle(lst)
        print(temp)
def sum_row(lst, low, high):
    if low < high:
        lst[low] += lst[low + 1]
        sum_row(lst, low+1, high)