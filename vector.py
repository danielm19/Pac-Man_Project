#Stephanie Becerra, id: 888771284
#Ryan Chen, id: 888611449
#Daniel Moran, id: 888769718

from distutils.log import error
from io import UnsupportedOperation
from math import sqrt

class Vector:
    '''General purpose, 2d vector class for use in moving objects in games
       it turns out linear algebra IS useful after all !
       uses Python's version of operator overloading  v.__add__(u) can be written as v + u
    '''
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.thresh = 0.000001
    def __repr__(self):                 
        return f'Vector({self.x},{self.y})'
    def __add__(self, other):                     # v + u
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):                     # v - u # edited sub to sub correctly
        return Vector(self.x - other.x, self.y - other.y)
    def __neg__(self):                            # -v
        return Vector(-self.x, -self.y)
    def __mul__(self, k):                         # v * k
        return Vector(k * self.x, k * self.y)
    def __rmul__(self, k):                        # k * v
        return self.__mul__(k)
    def __floordiv__(self, k):                    # v // k
        if k > 0: 
            return Vector(self.x // k, self.y // k)
        else:
            raise Exception("Trying to divide with invalid integer")
    def __truediv__(self, k):                     # v / k
        if k > 0:
            return Vector(self.x / k, self.y / k)
        else:
            raise Exception("Trying to divide with invalid integer")

    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False 

    def dot(self, other):            # dot product, length of self when projected on other
        return self.x * other.x + self.y * other.y
    def cross(self, other): raise UnsupportedOperation    # not supported at this time: requires 3d Vectors !
    def norm(self):                  # length of a vector
        return sqrt(self.dot(self))
    def magnitude(self):             # edited this one
        return sqrt(self.mag_sq(self))
    def unit_vector(self):            # v of unit length in same direction as v
        return self / self.magnitude()
    
    def x_val(self):
        return self.x
    
    def y_val(self):
        return self.y
    
    def convert_tuple(self):
        return self.x, self.y
    
    def convert_tuple_int(self):
        return int(self.x), int(self.y)
    
    def copy(self):
        return Vector(self.x, self.y)
    
    def mag_sq(self):
        return self.x ** 2 + self.y ** 2

    def __iadd__(self, other):         # v += u
        self.x += other.x
        self.y += other.y
        return self
    def __isub__(self, other):         # v -= u
        self += -other
        return self
    def __imul__(self, k):             # v *= k
        self.x *= k
        self.y += k
        return self

    def asInt(self):               # converts floats to ints if needed
        return int(self.x), int(self.y)

    def __str__(self):          #for debugging purposes
        return "<"+str(self.x)+", "+str(self.y)+">"



