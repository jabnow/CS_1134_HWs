# question 3 part a
def find_duplicates(lst):
    duplicates = []
    uniques = []
    for val in lst:
        if val not in uniques:
            uniques.append(val)
        else:
            duplicates.append(val)
    return duplicates

# question 3 part b
# analyze the worst case running time of q3 part a
