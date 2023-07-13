##### vector class
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# Max(5, 10) = 10

class Vector(object):
    def __init__(self, *args): # packing
        '''
        Create a vector, example : v = Vector(5, 10)
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args
            
    def __repr__(self):
        '''Return the vector informations'''
        return f'Vector({self._x}, {self._y})'
        
    def __add__(self, other):
        '''Return the vector added self and other'''
        return Vector(self._x + other._x, self._y + other._y )
    
    def __mul__(self, y):
        '''Return the vector added self and other'''
        return Vector(self._x * y, self._y * y )
   
    def __bool__(self): #  check 0, 0
        return bool(max(self._x, self._y))
        
# print(Vector.__init__.__doc__)
# print(Vector.__repr__.__doc__)
# print(Vector.__add__.__doc__)
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()
# v4 = Vector(23, 22, 13) # ValueError expected 2
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(bool(v1), bool(v2), bool(v3))