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