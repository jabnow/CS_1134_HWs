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