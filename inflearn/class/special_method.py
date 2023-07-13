##### Special methods == Magic methods == Built-in methods
##### basic
print(int)
print(float)
# Check all attributes and methods
print(dir(int))
print(dir(float))
n = 10
# print(type(n)) # class
## add
print(n + 100)
print(n.__add__(100))
# print(n.__doc__) # docstring
## boolean
print(n.__bool__())
print(bool(n))
## mul
print(n * 100)
print(n.__mul__(100))

##### Magic
class Fruit():
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def __str__(self):
        return f"Fruit Class Info : {self._name} , {self._price}"

    def __add__(self, x): # s1, s2
        # print("Called >> __add__")
        return self._price + x._price #
        # return (self._price + x._price) * 0.8 / 0.2 * 1.3
        
    def __sub__(self, x):
        # print("Called >> __sub__")
        return self._price - x._price
    
    def __le__(self, x): # the first lower less
        if self._price <= x._price:
            return True
        return False
        
    def __ge__(self, x): # the first higher huge
        if self._price >= x._price:
            return True
        return False        
        
    ## __eq__ # same
    ## __ne__ # different     
        
        
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

##### customerizing
print(s1._price + s2._price)
print(s1 + s2) # __add__
print(s1 - s2)
print(s2 - s1)
print(s1 >= s2)
print(s1)
print(s2)