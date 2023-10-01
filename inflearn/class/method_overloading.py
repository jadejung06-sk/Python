"""
method overloading
overloading : 동일 메소드 재정의, 네이밍 기능 예측 가능, 코드 절약하고 가독성 향상, 메소드 파라미터 기반 호출 방식
oop
multipledispatch

"""

##### Ex 1 - 동일 이름 메소드 사용 예제, 동적 타입 검사(즉, 런타임 중에 타입 에러가 발생하여 실행중에 알 수 있음, C는 정적 타입 검사)

class SampleA():
    def add(self, x, y): ## 파라미터의 개수에 따라 메소드 호출되는 것을 오버로딩이라고 함 (파이썬 미지원)
        return x + y
    
    def add(self, x, y, z): ## 파라미터의 개수에 따라 메소드 호출되는 것을 오버로딩이라고 함 (파이썬 미지원)
        return x + y + z
    
    ##### solution 1
    # def add(self, *args):
        # return sum(args)
    
   
a = SampleA()
# print('Ex 1 > ', a.add(2, 3)) ## TypeError: SampleA.add() missing 1 required positional argument: 'z'
print('Ex 1 > ', dir(a)) ##   ['__class__', , ,'add']
# print('Ex 1 > ', a.add(2, 3,4, ,5, 6, 7)) ## solution 1

##### Ex 2 - (단일 함수) 동일 이름 메소드 사용 예제, 자료형에 따른 분기 처리
class SampleB():
    def add(self, datatype, *args):
        if datatype == 'int':
            return sum(args)
        
        if datatype == 'str':
            return ' '.join([x for x in args])
        
        
b = SampleB()
print('Ex 2 > ',b.add('int', 5, 6))
print('Ex > ', b.add('str', 'Hi', 'Python'))

##### Ex 3 - multipledispatch
## pip install multipledispatch
## pip list
## pip search multipledispatch
from multipledispatch import dispatch

class SampleC():
    @dispatch(int, int)
    def product(x, y):
        return x * y
    
    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z
    
    @dispatch(float, float, float)
    def product(x, y, z):
        return x * y * z
    
c = SampleC()
print('Ex 3 > ', c.product(5, 6))
print('Ex 3 > ', c.product(5, 6, 7))
print('Ex 3 > ', c.product(5.0, 6.0, 7.0))