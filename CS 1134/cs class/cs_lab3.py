#coding question 1 pt a
def reverse_list(lst):
    #swap indeces, have two pointers from both ends
    i, j = 0, len(lst)-1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst

print(reverse_list([1, 2, 3, 4, 5]))
#[5, 4, 3, 2, 1]

#coding question 1 pt b
def reverse_list_mod(lst, low = None, high = None):
    if low or high == None: #and?
        low = 0
        high = len(lst)-1
    while low < high:
        lst[low], lst[high] = lst[high], lst[low]
        low += 1
        high -= 1
    return lst

lst2 = [1, 2, 3, 4, 5, 6]
low = 0
high = 5
print(reverse_list_mod(lst2))
#[6, 5, 4, 3, 2, 1]

lst3 = [1, 2, 3, 4, 5, 6]
low = 1
high = 3
print(reverse_list_mod(lst3, 1, 3))
#[1, 4, 3, 2, 5, 6]

#question 2
def move_zeros(nums):
    #if 0 store index in a new list (1st pointer, i)
    #then get elements to shift (2nd pointer, first)
    first = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i], nums[first] = nums[first], nums[i]
            first += 1
    return nums
#i think you can compare adjacent vals and move the lesser number back

lst = [0, 1, 0, 3, 13, 0]
print(lst)
print(move_zeros(lst))
#return [1, 3, 13, 0, 0, 0]

#question 3
def shift(lst,k): #right shift only
    reverse_list_mod(lst)
    reverse_list_mod(0, k-1)
    reverse_list_mod(lst, k, len(lst)-1)
    return lst
#this is like the homework question

#question 4
#make it crawl inside the window from the initial sum
#two pointers make the window, use max func

# Input: nums = [1,12,-5,-6,50,3], k = 3
# Output: 47
# Explanation: Maximum sum is (-6 + 50 + 3) = 47. The window size is 3
