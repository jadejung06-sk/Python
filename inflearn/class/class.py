##### Class 
## focus on data == Object

##### Old version 1
car_company_1 = "Ferrari"
car_detail_1 = [
    {'color':'White'},
    {'horsepower':400},
    {'price':8000}
]

car_company_2 = "BMW"
car_detail_2 = [
    {'color':'Black'},
    {'horsepower':270},
    {'price':5000}
]

car_company_3 = "Audi"
car_detail_3 = [
    {'color':'Silver'},
    {'horsepower':300},
    {'price':6000}
]

##### Old version 2
## Demerit : Index, delete
car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color':'White', 'horsepower':400, 'price':8000},
    {'color':'Black', 'horsepower':270, 'price':5000},
    {'color':'Silver', 'horsepower':300, 'price':6000}
]

del car_company_list[1]
del car_detail_list[1]
print(car_company_list)
print(car_detail_list)

print()
print()

##### dictionary strucuture
# Demerit : duplication, keyError
car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color':'White', 'horsepower':400, 'price':8000}},
    {'car_company': 'BMW', 'car_detail': {'color':'Black', 'horsepower':270, 'price':5000}},
    {'car_company': 'Audi', 'car_detail': {'color':'Silver', 'horsepower':300, 'price':6000}}
]

del car_dicts[1]
print(car_dicts)

##### Class structure
# resue, reduce the same codes

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    ##### Magic Methods
    
    # def __str__(self): # for users 
        # return f'str : {self._company} - {self._details}'
    
    def __repr__(self): # for developers
        return f'repr : {self._company} - {self._details}'
    
    #######################################################
        
car1 = Car('Ferrari',  {'color':'White', 'horsepower':400, 'price':8000} )
car2 = Car('BMW',  {'color':'Black', 'horsepower':270, 'price':5000})
car3 = Car('Audi',  {'color':'Silver', 'horsepower':300, 'price':6000})

print(car1)
print(car2)
print(car3) 
# <__main__.Car object at 0x000001F9E8A0BFD0>
# __str__ : Ferrari - {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}} # top Priority
# 

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)
print(dir(car1))