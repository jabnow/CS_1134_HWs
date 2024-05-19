from ArrayQueue import ArrayQueue

# python's built in queue
'''
from queue import Queue

q = Queue() 
q.enqueue    --> q.put()
q.dequeue    --> q.get()
q.first/front--> q.queue[0]
q.is_empty   --> q.empty()
len(q)       --> q.qsize()

'''


# Question 1
def eval_prefix(exp_str):
    operators = '+-*/'
    exp_lst = exp_str.split()
    args_stack = ArrayStack()
    # Iterating from the back to the front
    for i in range(len(exp_lst)-1, -1, -1):
        token = exp_lst[i]
        # If token is an argument (a number)
        if token not in operators:
            args_stack.push(int(token))
        # If token is an operator:
        # this means we have two arguments in our stack already
        else:
            arg1 = args_stack.pop()
            arg2 = args_stack.pop()
            if (token == '+'):
                res = arg1 + arg2
            elif (token == '-'):
                res = arg1 - arg2
            elif (token == '*'):
                res = arg1 * arg2
            else: # token == '/'
                if arg2 == 0:
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            args_stack.push(res)

    return args_stack.pop()

# Another version of solution (left to right)
"""
def eval_prefix(exp_str):
    operators = '+-*/'
    exp_lst = exp_str.split()
    args_stack = ArrayStack()

    for token in exp_lst:
        if token in operators:  # always push operators to stack
            args_stack.push(token)
        else:  # number -> either do calculation or pop from the stack
            token = int(token)

            repeat = False
            # if the top of the stack is a number, pop it and the operator
            # to do the calculation
            # this process may need to be repeated if the top of the stack
            # is still a number
            if not args_stack.is_empty() and type(args_stack.top()) != str:
                repeat = True
            while repeat:
                repeat = False
                left_num = args_stack.pop()  # first digit in calculation
                operator = args_stack.pop()  # operator in calculation
                token = calculate(left_num, token, operator)
                # if top of stack is still a number, repeat the process
                if not args_stack.is_empty() and type(args_stack.top()) != str:
                    repeat = True
            # after calculation is done, push the result to the stack
            args_stack.push(token)
    return args_stack.pop()

def calculate(arg1, arg2, operator):
    if (operator == '+'):
        res = arg1 + arg2
    elif (operator == '-'):
        res = arg1 - arg2
    elif (operator == '*'):
        res = arg1 * arg2
    else: # token == '/'
        if arg2 == 0:
            raise ZeroDivisionError
        else:
            res = arg1 / arg2
    return res
"""

print("\nTESTING Q2:")
print(eval_prefix("1134"))  # edge case, just num
print(eval_prefix(" - + * 16 5 * 8 4 20"))
print(eval_prefix("+ * 5 5 / 10 2"))
print(eval_prefix("+ / - 10 2 4 8"))
print(eval_prefix("+ * 6 3 * 8 4"))
print(eval_prefix("- + * 8 2 4 +  3 6"))
print(eval_prefix("+ + + + 1 2 3 4 5 "))  # edge case, all ops in front, all nums in back




# QUESTION 2
import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue_first(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.front_ind = (self.front_ind - 1) % len(self.data)
            self.data[self.front_ind] = elem
            self.num_of_elems += 1

    def enqueue_last(self, elem):
        if(self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.back_ind = (self.back_ind + 1) % len(self.data)
            self.data[self.back_ind] = elem
            self.num_of_elems += 1

    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        elif(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def dequeue_last(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.back_ind]
        self.data[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        elif(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.back_ind]

    def resize(self, new_cap):
        old_data = self.data
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            new_data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.data = new_data
        self.front_ind = 0
        self.back_ind = self.front_ind + self.num_of_elems - 1




# QUESTION 3
def flatten_list_by_depth(lst):
    # basically breadth first search, which you'll learn in binary trees topic
    q = ArrayQueue()
    new_lst = []

    for elem in lst:  # push all elem from lst to queue
        q.enqueue(elem)

    while not q.is_empty():
        length = len(q)  # get current length for at curr depth

        for i in range(length):
            front = q.dequeue()

            if isinstance(front, list):
                for elem in front:  # take off one layer of nesting
                    q.enqueue(elem)  # put all elem back into the end of queue

            elif isinstance(front, int):
                new_lst.append(front)  # append to new lst, don't put back into queue

    return new_lst


lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
new_lst = flatten_list_by_depth(lst)




# QUESTION 4
# A. Push Operation Θ(1) however pop is costly
class Stack1:
    def __init__(self):
        self.queue = ArrayQueue()

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return self.queue.is_empty()

    def push(self, data):
        self.queue.enqueue(data)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        for i in range(len(self.queue) - 1):  # shift the last element to the front and then pop
            x = self.queue.dequeue()
            self.queue.enqueue(x)
        return self.queue.dequeue()

    def top(self):
        for i in range(len(self.queue) - 1):  # shift the last element to the front
            x = self.queue.dequeue()
            self.queue.enqueue(x)

        val = self.queue.first()  # save it
        self.queue.enqueue(self.queue.dequeue())  # put it back in the end
        return val  # return the saved value


# B. Pop Operation  Θ(1) however push is costly
class Stack2:  # Second Implementation
    def __init__(self):
        self.queue = ArrayQueue()

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return self.queue.is_empty()

    def push(self, data):
        self.queue.enqueue(data)
        for i in range(len(self.queue) - 1):  # shift the ordering to maintain LIFO order instead of FIFO
            x = self.queue.dequeue()  # n^2 cost
            self.queue.enqueue(x)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.queue.dequeue()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.queue.first()




# QUESTION 5 -- WHAT IS THISS
    # here we have 2 input values so our run-time/space complexity is with respect to n and k
def n_bonacci(n, k):  # n - bonacci sequence type, k - the first k values of the sequence
    queue = ArrayQueue()
    total = n  # curr total, if fibbonaci, queue has [1, 1], and the curr total is 2 ... etc
    for i in range(k):
        if i < n:  # first couple of 1's, the sequence starts off with n 1's
            queue.enqueue(1)  # if n = 2 (fibbonaci), there will be 2 1's,
            yield 1  # if n = 3, there will be 3 1's, etc ...
        else:
            queue.enqueue(total)
            yield total
            total = 2 * total - queue.dequeue()  # update total efficiently


# run-time for this is O(k) - generating the first k values of the sequence
# extra space complexity is O(n) - holding only n numbers at a time


'''
explaining the total = 2*total - queue.dequeue()

if 4 bonnacci --> first 9 values
#1, 1, 1, 1, 4, 7, 13, 25, 49
49 =  4 + 7 + 13 + 25, if you take a look at the prev total, 13

so we're really adding      1 + 4 + 7  +    (1 + 1 + 4 + 7) <-- this last one is 13

notice that prev total, 13 = (1 + 1 + 4 + 7) is basically the sum of the previous 3, but with an extra value, the first value,
so, we can double it as (1 + 1 + 4 + 7) + (1 + 1 + 4 + 7), and remove that firs tvalue
--> (1 + 1 + 4 + 7) + (1 + 1 + 4 + 7)  - 1


1, 1, [1, 1, 4, 7], 13, 25, 49 #13 is the sum of the values in the brackets
1, 1, 1, [1, 4, 7, 13], 25, 49   #25 is the sum of the values in the brackets

'''

print("\nTesting 4, 9")
for i in n_bonacci(4, 9):
    print(i, end=" ")

print("\nTesting 4, 2")
for i in n_bonacci(4, 2):
    print(i, end=" ")

print("\nTesting 2, 10")
for i in n_bonacci(2, 10):
    print(i, end=" ")

print("\nTesting 2, 1")
for i in n_bonacci(2, 1):
    print(i, end=" ")


