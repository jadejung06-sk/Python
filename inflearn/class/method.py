class Car():
    """
    Car class
    Author : Jade
    Date:2023.07.12    
    """
    ##### Class Variables (all instances share these variables)
    car_count = 0
    
    ###### Instance Variables
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1    

    ###### Instance methodss   
    def __str__(self): # for users 
        return f'str : {self._company} - {self._details}'
    
    def __repr__(self): # for developers
        return f'repr : {self._company} - {self._details}'
    
    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")
    
car1 = Car('Ferrari',  {'color':'White', 'horsepower':400, 'price':8000} )
car2 = Car('BMW',  {'color':'Black', 'horsepower':270, 'price':5000})
car3 = Car('Audi',  {'color':'Silver', 'horsepower':300, 'price':6000})

print((id(car1)))
print((id(car2)))
print((id(car3)))

print(car1._company == car2._company)
print(car1 is car2)

##### dir & __dict__
## all methods (List)
print(dir(car1))
print(dir(car2)) 
## instance attributes (Dict)
# self == itself
print(car1.__dict__)
print(car2.__dict__)

###### Doctring
print(car1.__doc__)

###### methods
# TypeError : Car.detail_info()
Car.detail_info(car1)
Car.detail_info(car2)
Car.detail_info(car3)
car1.detail_info()
car2.detail_info()
car3.detail_info()

##### Class
## all the same
print(id(car1.__class__), id(car2.__class__), car3.__class__)
print(car1.car_count)
print(car2.car_count)
print(car3.car_count)
print(Car.car_count)
##### __del__
del car2
print(car1.car_count)
# print(car2.car_count)
## Variables : Instance(self) -> Class -> Error
print(car3.car_count)
print(Car.car_count)