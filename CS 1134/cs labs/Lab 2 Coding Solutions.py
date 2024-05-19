
'''
CS1134 LAB 1 SOLUTIONS
There are many solutions to these questions. 
I recommend having students post their own on the board.
Also make sure to tell students to use good variable names, and use snake_case or camelCase.
'''

# QUESTION 1

def powers_of_two(n):
    for i in range(n):
        yield 2**i

        
# QUESTION 2

class Polynomial:
    def __init__(self, lst = None):
        # Note: do not do lst = [0] as a default argument!
        # Read more here: https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
        if lst = None:
            lst = [0]
        self.data = lst

    def __call__(self, val):
        # val = x, x^power * coefficient
        return sum([(val**i)*self.data[i] for i in range(len(self.data))])

    def __add__(self, other):
        lst = self.data.copy()
        temp = other.data.copy()
        
        if len(lst) > len(temp):
            lst, temp = temp, lst   # have lst be the shorter one

        while len(lst) < len(temp): # extend lst (the shorter one) with 0's
            lst.append(0)
            
        lst = [lst[i] + temp[i] for i in range(len(lst))]
        return Polynomial(lst)
        
# OPTIONAL

    def __repr__(self):
        return " + ".join([str(self.data[i])+"x^"+str(i) for i in range(len(self.data)-1, -1, -1)])

    def __mul__(self, other):
        lst = [0]*(len(self.data) + len(other.data))

        for i in range(len(self.data)):
            for j in range(len(other.data)):
                lst[i+j] += self.data[i] + other.data[j]
        return Polynomial(lst)

    def derive(self):
        for i in range(1, len(self.data)):
            self.data[i - 1] = self.data[i]*(i)
        self.data.pop()

# QUESTION 3

class UnsignedBinaryInteger:
    def __init__(self, bin_num_str):
        self.data = bin_num_str

    # reused code from lab 1
    def __add__(self, other):
        result = ""
        carry = 0

        max_length = max(len(self.data), len(other.data))

        # sign extension so both will have same length
        b1 = (max_length - len(self.data))*'0' + self.data
        b2 = (max_length - len(other.data))*'0' + other.data
 
        for i in range(1, max_length + 1):
            # we will use the negative indices since we evaluate from right to left
            sum_bits = int(b1[-i]) + int(b2[-i]) + carry
            result = str(sum_bits % 2) + result

            # can replace this with carry = sum_bits >= 2
            if sum_bits < 2:
                carry = 0
            else:
                carry = 1   # if sum of the bits + carry >= 2, then carry = 1

        result = carry*'1' + result

        return UnsignedBinaryInteger(result)

    def decimal(self):
        value = 0
        for i in range(len(self.data)):
            value += int(self.data[i]) * 2** (len(self.data) - 1 -i)
        return value
        # one line comprehension syntax
        # return sum(int(self.data[i]) * 2** (len(self.data) - 1 -i) for i in range(len(self.data)))

    # self < other
    def __lt__(self, other):
        # more digits = greater value. longer the str = more digits
        if len(self.data) < len(other.data):
            return True

        elif len(self.data) > len(other.data):
            return False

        # same number of digits
        for i in range(len(self.data)):
            if self.data[i] != other.data[i]:
                return self.data[i] == '0'  # if both not equal, that means one bin num has a 1, other has a 0
                                            # if self has a 0, that means itâ​​s the smaller one

        return True # no differences in digits detected

    #self > other
    def __gt__(self, other):    # self is not (less than other), implies it is greater or equal, check not equal to make sure
        return not ((self < other) or self == other)

    #self == other
    def __eq__(self, other):    # only way to have equal value is to have same bin num str for data
        return self.data == other.data
        
    def is_twos_power(self):
        # recall that the only way for a bin_num to be 2's power is if only the first digit is 1 and the rest are 0's

        # skip the first digit as it is always 1, check the remaining digits. If the sum of those digits == 0, we have a 2's power.
        remaining_sum = 0
        for i in range(1, len(self.data)):
            remaining_sum += self.data[i] == '1'    # implicit conversion; 0 if false, 1 if true
            
        return remaining_sum == 0   # 0 sum indicates all 0's for the remaining digits
        
    def largest_twos_power(self):
        # this is a more intuitive solution
        largest_sum = 1
        value = int(self)

        while largest_sum*2 <= value:
            largest_sum *= 2
            
        return largest_sum
        
    def __repr__(self):
        return "0b"+self.data

    # OPTIONAL
    # CODING PART 4 (not the best solution but ya boi is sleepy @ 1AM)

    # use 0 for sign extension
    def __and__(self, other):
        result = ""

        shorter = self.data
        longer = other.data

        if longer < shorter:
            shorter, longer = longer, shorter   # swap
            
'''
10011 --> 10011
100 --> 00100, sign extension
000 --> result = 0
we only need to check as many digits as there are for the shorter one
we can sign extend the shorter one to 0, but since 0 and with 0, 1 == 0, we don't need to bother with 10, and only compare 011 with 100
it is also okay to just do the sign extension and attach the excess 0's as they will be removed in the while loop below '''

        for i in range(len(shorter)):
            # make sure to account for the difference in length
            # can replace this if/else with result += int(shorter[i] == '1' and longer[i + len(longer) - len(shorter)] == '1')
            if (shorter[i] == '1' and longer[i + len(longer) - len(shorter)] == '1'):
                result += '1'
            else:
                result += '0'
                
        while len(result) > 1 and result[0] != '1': # get rid of excess leading 0's
            result = result[1:]
        
        return UnsignedBinaryInteger(result)
        
    def __or__(self, other):
        result = ""
        max_length = max(len(self.data), len(other.data))

        #sign extension so both will have same length
        b1 = (max_length - len(self.data))*'0' + self.data
        b2 = (max_length - len(other.data))*'0' + other.data
        
'''
10011 --> 10011

100 --> 00100, sign extension 10111 --> result = 0
in the case of or, it is easier to use sign extension '''

        for i in range(max_length):

        # can replace this if/else with result += int(b1[i] == '1' or b2[i] == '1')
        if b1[i] == '1' or b2[i] == '1':
            result += '1'
        else:
            result += '0'
            
        while len(result) > 1 and result[0] != '1': #get rid of excess leading 0's
            result = result[1:]

        return UnsignedBinaryInteger(result)
