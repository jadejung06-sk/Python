class Car():
    """
    Car class
    Author : Jade
    Date:2023.07.12
    Description : class, static, instance method
    """
    ##### Class Variables (all instances share these variables)
    price_per_raise = 1.0
    
    ###### Instance Variables
    def __init__(self, company, details):
        self._company = company
        # self.car_count = 10
        self._details = details
        # Car.car_count += 1    

    ###### Instance methods(self)
    ## self == object   
    def __str__(self): # for users 
        return f'str : {self._company} - {self._details}'
    
    def __repr__(self): # for developers
        return f'repr : {self._company} - {self._details}'
    
    def get_price(self):
        return f"Before Car Price -> company : {self._company}, price : {self._details.get('price')}"
    
    def get_price_culc(self):
        return f"After Car Price -> company : {self._company}, price : {self._details.get('price') * Car.price_per_raise }"

    
    # def __del__(self):
        # Car.car_count -= 1

    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")
        
    ##### Class Methods
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or more')
            return
        cls.price_per_raise = per
        print('Succeed! Price Increased.')
        
    ##### Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return f'OK! This car is {inst._company}'
        return f'Sorry! This car is not BMW.'
    
    
car1 = Car('Ferrari',  {'color':'White', 'horsepower':400, 'price':8000} )
car2 = Car('BMW',  {'color':'Black', 'horsepower':270, 'price':5000})
car3 = Car('Audi',  {'color':'Silver', 'horsepower':300, 'price':6000})


############################ method 1 (no class)
car1.detail_info()
car2.detail_info()
print(car1._details.get('price'))
print(car2._details['price'])
##### Before rasing
print(car1.get_price())
print(car2.get_price())
##### After rasing
## price_per_raise 
Car.price_per_raise = 1.4
print(car1.get_price_culc())
print(car2.get_price_culc())
############################## method 2-1 (class)
Car.raise_price(1.6)
print(car1.get_price_culc())
print(car2.get_price_culc())
############################## method 2-2 (class + static method - not important)
## instance
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
## class
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))