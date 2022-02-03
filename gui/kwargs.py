### *args practice
def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

# print(add(4,2))

### **kwargs practice
def calculate(n, **kwargs):
    # print(type(kwargs))
    # print(kwargs)
    # print(kwargs["add"])
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs['multiply'] # ★
    print(n)

# calculate(2, add = 3, multiply = 5)

### class & **kwargs practice

# class Car:

#     def __init__(self, **kwargs):
#         self.make = kwargs["make"]
#         self.model = kwargs["model"]
        
# my_car = Car(make= "Nissan", model = "GT-R")
# # my_car_2 = Car(make= "Nissan") # ★
# print(my_car.model) # ★
# # print(my_car_2) # KeyError : 'model'


class Car_2:
    
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats") # ★
        
my_car2 = Car_2(make= "Nissan")
print(my_car2.make)
print(my_car2.model) # None