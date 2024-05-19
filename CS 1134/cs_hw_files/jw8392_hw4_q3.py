# QUESTION 3 PART A
def print_triangle(n):
    if n == 0:
        return
    else:
        print_triangle(n - 1)
        print('*'*n)


# QUESTION 3 PART B
def print_opposite_triangles(n):
    if n == 0:
        return
    else:
        print('*'*n)
        print_opposite_triangles(n-1)
        print('*'*n)


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