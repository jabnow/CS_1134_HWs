# QUESTION 3 PART A
def print_triangle(n):
    if n == 1:
        return '*' + '\n'
    else:
        curr_row = print_triangle(n-1)
        curr_tri = '*'*n + '\n'
    return curr_row + curr_tri


# QUESTION 3 PART B
def print_opposite_triangle(n):
    if n == 0:
        return '*' + '\n'
    else:
        print('*'*n)
        print_opposite_triangle(n-1)
        print('*'*n)
#there's an extra None, but should be ok?


# QUESTION 3 PART C
def print_ruler(n):
    if n == 0:
        print()
    elif n == 1:
        print('-')
    else:
        print_ruler(n-1)
        print('-'*n)
        print_ruler(n-1)

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


# QUESTION 5
def count_lowercase(s, low, high):
    if low >= high:
        return 0
    else:
        count = sum(1 for let in s if let.islower())
    return count



def is_number_of_lowercase_even(s, low, high):
    if low >= high:
        return
    else:
        if count_lowercase(s, low, high) % 2 == 0:
            return True
        else:
            return False



# QUESTION 6
def appearances(s, low, high):
    '''
        The function should return a dictionary that stores a mapping of characters to the
    number of times they each appear in s.
        '''
    my_dict = {}
    keys = list(s)

    for ele in keys:
        if low >= high:
            return
        else:
            let_count = 0
            for i in range(len(s)-1):
                if s[low] == ele:
                    let_count += 1
                else:
                    let_count += appearances(s, low+1, high)
                keys[i] = let_count
            # appearances(s, low + 1, high)
            # my_dict[ele] = sum(1 for let in s)
            # need to sum up for each letter

    return my_dict

s2 = 'Hello World'
lowest = 0
highest = len(s2)-1
print('i messed up the counting for dictionary: ')
#print(appearances(s2, lowest, highest))

# QUESTION 7
def split_by_sign(lst, low, high):
    if low >= high:
        return 'it good'

    if lst[low] < 0:
        split_by_sign(lst, low+1, high)
    if lst[high] >= 0:
        split_by_sign(lst, low, high-1)
    else:
        lst[low], lst[high] = lst[high], lst[low]
        split_by_sign(lst, low+1, high-1)  # or high-1 here
    return lst

# QUESTION 8
def flat_list(nested_lst, low, high):
    res_lst = []
    for i in range(low, high + 1):
        if isinstance(nested_lst[i], int):
            res_lst.extend([nested_lst[i]])
        else:
            undo_nest = flat_list(nested_lst[i], low, len(nested_lst[i])-1)
            res_lst.extend(undo_nest)
    return res_lst



# QUESTION 9 (OPTIONAL)
def permutations(lst, low, high):
    res_lst = []
    if low >= high:
        return [lst[low]]
    else:
        for thing in permutations(lst, low+1, high):
            for i in range(low, high):
                ele = [lst[0:i]]
                fill_ins = [lst[i]] + [num for num in lst if num != lst[i]]
                # how do I make lst[i] rotate positions
                res_lst.append(ele + lst[i] + fill_ins)
    return res_lst

# P = n! / (n-r)! actually n! combos
# (n-1)! positions for each value

# but how to get each one?
oof = [1, 2, 3]
print('this one is really messed up: ')
print(permutations(oof, 0, 2))

