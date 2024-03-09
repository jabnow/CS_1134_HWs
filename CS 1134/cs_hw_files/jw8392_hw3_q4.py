#question 4 part b
def remove_all(lst, value):
    # return [ele for ele in lst if ele != value]

    count_targets = 0
    non_target_place = 0
    for i in range(len(lst)):
        if lst[i] == value:
            count_targets += 1
        if lst[i] != value:
            lst[i], lst[non_target_place] = lst[non_target_place], lst[i]
            non_target_place += 1
    for i in range(count_targets):
        lst.pop()
    return lst