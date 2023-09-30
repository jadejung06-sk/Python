"""
Property(2) - Getter, Setter
@property
: 파이써닉한 코드, 변수 제약 설정, getter, setter 효과 동등하여 코드 일관성 존재

getter, setter : 캡슐화-유효성 검사 기능 추가 용이, 대체 표현으로 내부의 표현 숨기기 가능, 속성의 수명 및 메모리 관리 용이
"""

##### Ex 1
# Proerty 활용, Getter, setter 작성

class SampleA:
    def __init__(self) -> None:
        self.x = 0
        self.__y = 0 # private
        
    @property 
    def y(self): ## == get_y() 변수마다 함수로 만들어야 하는 단점이 존재하기에 @property 활용, 언더스코어__ 제외
        print('Called get method.') ## 확인용
        return self.__y
    @y.setter
    def y(self, value): ## == set_y(value), 언더스코어__ 제외
        print('Called set method.') ## 확인용
        self.__y = value    
    @y.deleter
    def y(self):
        del self.__y
    
    
a = SampleA()

a.x = 1
a.y = 2 ## 변경 called set method

print('Ex 1 > {}'.format(a.x))
print('Ex 1 > {}'.format(a.y)) ## 읽기 called get method
print('Ex 1 > ', dir(a)) # _SampleA__y 존재
del a.y
print('Ex 1 > ', dir(a)) # _SampleA__y 제외

##### Ex 2
class SampleB:
    def __init__(self) -> None:
        self.x = 0
        self.__y = 0 # private
        
    @property 
    def y(self): ## == get_y() 변수마다 함수로 만들어야 하는 단점이 존재하기에 @property 활용, 언더스코어__ 제외
        print('Called get method.') ## 확인용
        return self.__y
    @y.setter
    def y(self, value): ## == set_y(value), 언더스코어__ 제외
        if value < 0:
            raise ValueError('Input a value higher than 0.')
        print('Called set method.') ## 확인용
        self.__y = value    
        
    @y.deleter
    def y(self):
        del self.__y
        
b = SampleB()
b.x = 1
b.y = 10
# b.y = -5 # 예외 발생

print('Ex 2 > {}'.format(b.x))
print('Ex 2 > {}'.format(b.y)) ## 읽기 called get method
print('Ex 2 > ', dir(b)) # _SampleA__y 존재
del b.y
print('Ex 2 > ', dir(b)) # _SampleA__y 제외
