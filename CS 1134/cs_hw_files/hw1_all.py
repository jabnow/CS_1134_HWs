#Q2
def shift(lst, k, direction='left'):
    if direction == 'left':
        lst2 = [0] * len(lst)
        for i in range(len(lst) - 1, -1, -1):
        #just assign values to lst2
            lst2[i-k] = lst[i]
        for i in range(len(lst)):
        #assign values in lst2 to lst
            lst[i] = lst2[i]
        return lst
    elif direction == 'right':
        lst2 = []
        #the elements that rotate to the front
        for i in range(len(lst)-k, len(lst)):
            lst2.append(lst[i])
        #the other elements are displaced
        for i in range(0, len(lst)-k):
            lst2.append(lst[i])
        #reassign to original list
        for i in range(0, len(lst)):
            lst[i] = lst2[i]
        return lst


#Q3
#question 3 part a
def sum_square(n):
    tup = (range(0, n, 1))
    count = 0
    for thing in tup:
        thing **= 2
        count += thing
    return count

#question 3 part b
def sum_square2(n):
    #uses list comprehension
    return sum(i**2 for i in range(0, n))

#question 3 part c
def sum_square_odd(n):
    i = 1
    total = 0
    while i < n:
        if i % 2 == 1:
            total += i**2
            i += 2
    return total

#question 3 part d
def sum_square_odd2(n):
    return sum(i**2 for i in range(1, n, 2) if i % 2 == 1)

#Q4
#question 4 part a
def ten_powers(n=10):
    return(list(n**i for i in range(0, 6)))

#question 4 part b
def adj_multiplier(i):
    return(list(i*(i+1) for i in range(0, 10)))

#part c by list comprehension
def alphabet():
    return(list(chr(i) for i in range(97, 124)))

#Q5
#question 5
def fibs(n):
    n1, n2 = 1, 1
    if n <= 0:
        yield "bruh"
    elif n <= 1:
        yield 1
    else:
        for i in range(0, n):
            yield n1
            nxt = n1 + n2
            n1, n2 = n2, nxt

#Q6
#question 6
class Vector:
    #given info
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0] * d
        elif isinstance(d, (list, tuple)):
            self.coords = d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "<"+ str(self.coords)[1:-1] + ">"

    def __repr__(self):
        return str(self)
    #end given info

    #part b
    def __sub__(self, other):
        newV = Vector(len(self.coords))
        #check length
        if len(self.coords) == len(other.coords):
            for i in range(len(newV.coords)):
                newV.coords[i] = self.coords[i] - other.coords[i]
            return newV
        else:
            raise ValueError("boo...")

    #part c
    def __neg__(self):
        newV = Vector(len(self.coords))
        for i in range(len(newV.coords)):
            newV[i] = self.coords[i]*(-1)
        return newV


    #part d
    def __mul__(self, other):
        newV = Vector(len(self.coords))
        if isinstance(other, int): #scalar product
            for i in range(len(self.coords)):
                newV.coords[i] = self.coords[i] * other
            return newV
        elif len(other.coords) == len(self.coords): #dot product
            # part f
            count = 0
            for i in range(len(self.coords)):
                newV.coords[i] = self.coords[i] * other.coords[i]
                count += newV.coords[i]
            return count
        else:
            raise ValueError("boo...")

    #part e
    #reverse of the dot product also
    def __rmul__(self, num):
        newV = Vector(len(self.coords))
        if isinstance(num, int):
            for i in range(len(self.coords)):
                newV.coords[i] = self.coords[i] * num
            return newV
        elif len(num.coords) == len(self.coords): #dot
            # part f
            count = 0
            for i in range(len(self.coords)):
                newV.coords[i] = self.coords[i] * num.coords[i]
                count += newV.coords[i]
            return count
        else:
            raise ValueError("boo...")