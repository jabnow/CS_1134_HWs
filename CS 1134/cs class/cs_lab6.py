#Recursion day

#q1: function that returns the sum of all numbers 0-->5
def sum_to(n):
    sum = 0
    if n==0:
        return n
    else:
        sum = sum_to(n-1)+n
    return sum
print(sum_to(5))

#q2: the product of all even numbers 1-->n (n is even)
def product_evens(n):
    curr_prod = n
    if n==0:
        return 1
    else:
        curr_prod *= product_evens(n-2)
    return curr_prod
print(product_evens(8))

#q3: find the max in non-empty, non-sorted list of nums
#part a: the runtime is n^2?
#each comparison: n, n-1, n-2, n-3, n-4....4, 3, 2, 1 = theta(n^2)

#part b: function includes low and high parameters
#must run in linear time
def find_max(lst, low, high):
    temp_max = 0
    if low == high:
        return lst[high]
    if lst[low] > find_max(lst, low+1, high):
        return lst[low]
    else:
        temp_max = find_max(lst, low+1, high)
    return temp_max

lst = [1, 7, 10, 9, 3, 4, 5]
low = 0
high = len(lst)-1
print(find_max(lst, low, high))

#q4: valid palindrome, returns a boolean
def is_palindrome(stri, low, high):
    if stri[low] != stri[high]:
        return False
    elif low >= high:
        return True
    else:
        return (is_palindrome(stri, low+1, high-1))
stri = 'racecar'
low = 0
high = len(stri)-1
print(is_palindrome(stri, low, high))

#5: find a target in a sorted list with binary search
#otherwise return None
def binary_search(lst, low, high, val):
    if len(lst)==0:
        return None
    if val not in lst:
        return None
    mid = (high+low) // 2
    if lst[mid] == val:
        return mid
    elif lst[mid] < val: # look on the right
        target = binary_search(lst,mid+1, high, val)
    else: #look on the left
        target = binary_search(lst, low, mid, val)
    return target

lst1 =  [1, 3, 4, 5, 9, 12]
lo = 0
hi = len(lst1)-1
val = 3
print(binary_search(lst1, lo, hi, val))

#Q6: returns tuple of 2 ints: number of vowels, number of consonants
#create a new tuple to return each time when updating counts
#must be linear runtime

def vc_count(word, low, high):
    if low == high:
        chara = word[low]
        vow_count = len(list(chara for chara in word if chara in 'AaEeIiOoUu'))
        return (vow_count, 0)
    else:
        cons_count = len(list(chara for chara in word if chara not in 'AaEeIiOoUu'))
        return (0, cons_count)

    first_vow = vc_count(word, low, low)[0]
    change_vow = vc_count(word, low+1, high)[0]
    first_cons = vc_count(word, low, low)[1]
    change_cons = vc_count(word, low+1, high)[1]
    return(first_vow+change_vow, first_cons+change_cons)

wordo = "NYUTandonEngineering"
long = len(list(wordo))-1
print(vc_count(wordo, 0, long))


#vitamins answers
# q1:
# a) 80 final, each call is constant: theta(n)
# b) 5 final, each call is constant: theta(log(n))
# c) 36 final, each call is slices of n-1: theta(n^2)