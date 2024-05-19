from ArrayStack import ArrayStack


# Q1
def stack_sum(s):
    if len(s) == 0:
        return 0
    else:
        val = s.pop()
        curr_total = stack_sum(s)
        curr_total += val
        s.push(val)
        return curr_total


# Q1v2
def stack_sum2(s):
    total = 0
    if not s.is_empty():  # len(s) != 0
        val = s.pop()
        total = val + stack_sum2(s)
        s.push(val)
    return total


print("\nTESTING Q1:")
s = ArrayStack()  # stack already sorted
for i in range(9, 0, -1):
    s.push(i)
print(stack_sum(s))
print(stack_sum2(s))


# Q2
class MeanStack:
    def __init__(self):
        self.data = ArrayStack()
        self.ssum = 0

    def __len__(self):
        # Return the number of elements in the stack
        return len(self.data)

    def is_empty(self):
        # Return​ True​ if stack is empty
        return self.data.is_empty()

    def push(self, e):
        #​Add​element e to the end of the stack.
        # If e is not an int or float, raise a TypeError
        if not(isinstance(e, int) or isinstance(e, float)):
            raise TypeError
        self.data.push(e)
        self.ssum += e

    def pop(self):
        # Remove​ and​ return​ the last element from​ the stack.
        # If​ the stack is​ empty,​ raise an exception
        if self.is_empty():
            raise Exception("Empty Mean Stack")
        ret = self.data.pop()
        self.ssum -= ret
        return ret

    def top(self):
        # Return​a reference to the last element of the stack without removing it.
        # If the stack is empty, raise an exception
        if self.is_empty():
            raise Exception("Empty Mean Stack")
        return self.data.top()

    def sum(self):
        # Returns the sum of all values in the stack
        return self.ssum

    def mean(self):
        # Return the mean value in the stack
        return self.ssum / len(self)

# Q3
'''
the idea is to use the stack to store the int values in reverse order

start from the back because stack reverses the order and it's more efficient to remove from the back than it is from the front
is the last elem a list? if so, pop it and extend it back onto the list
is the last elem an instead? if so, store it into the stack

repeat this until the list is empty
then pop all values from the stack and add them back onto the list

'''


def flatten_lst(lst):
    stack = ArrayStack()

    while len(lst) != 0:
        val = lst.pop()  # get the last value
        if isinstance(val, list):  # is it a list?
            lst.extend(val)  # extend it back AND REMOVES ONE LAYER

        else:  # it's an int, its already flattened
            stack.push(val)

    while not stack.is_empty():
        lst.append(stack.pop())  # remove the values from the stack and place back into the list


print("\nTESTING Q3:")
lst = [1, [2, 3, 4], [5, [6, [7]], [8, [[9]]]]]
print(lst)
flatten_lst(lst)
print(lst)


# Q4
'''
the idea is to store to have the other stack store the values in descending order
ex stack top <-> bottom

s = [1, 5, 8, 2, 5, 9, 2]

helper = [1] 
helper = [5, 1]     5 > 1
helper = [8, 5, 1]  8 > 5
helper = [8, 5, 1]  2 > 8 is false, store 2 in temp var

put the values from helper back onto stack until temp > helper.top()
helper = [5, 1]
helper = [1] 2 > 1 so we can put the value of temp onto the helper stack now
helper = [2, 1]

repeat this process
helper = [5, 2, 1]
helper = [8, 5, 2, 1]
... so on 

'''


def stack_sort(s):  # DRAW A DIAGRAM WHEN PLANNING
    helper = ArrayStack()

    while not s.is_empty():  # ORIGINAL STACK EXISTS
        temp = s.pop() # DECIDED WHERE CURRENT VALUE GOES

        while (not helper.is_empty()) and temp < helper.top(): # IF LESS THAN SMALLEST VAL IN HELPER
            s.push(helper.pop()) # PUT IT BACK IN THE ORIGINAL, IN ORDER

        helper.push(temp) # IF IT'S BIGGER, ORDER IT IN HELPER

    while not helper.is_empty(): # CLEAN UP, PUSH ALL INTO ORIGINAL
        s.push(helper.pop())
        

print("\nTESTING Q4:")
s = ArrayStack()  # stack already sorted
for i in range(9, 0, -1):
    s.push(i)

s2 = ArrayStack()  # descending order stack, worst case O(n^2)
for i in range(1, 10):
    s2.push(i)

s3 = ArrayStack()  # don't actually do this... I'm just lazy so lol
s3.data = [4, 9, 2, 1, 4, 6, 8, 1, 7, 11, 23, 5, 7]

print(s.data)
stack_sort(s)
print(s.data)

print(s2.data)
stack_sort(s2)
print(s2.data)

print(s3.data)
stack_sort(s3)
print(s3.data)


