"""
property(1) - underscore
access modifier(접근지정자), underscore

다양한 언더스코어 활용
파이썬 접근지정자 설명
1. 인터프리터 2. 값 무시 3. 네이밍 (국제화, 자릿수)
"""
##### Ex 1 - 값 무시
x, _, y = (1, 2, 3)
print(x, y)
a, *_, b = (1, 2,3, 4, 5)
print(a, b)
for _ in range(10):
    pass
for _,  val in enumerate(range(10)):
    pass

##### Ex 2 - 접근지정자 : 약속된 규약으로 강제는 아닌 장려 (중요)
# name = public variable
# _name = protected variable
# __name = private variable
## 타 클래스 (클래스 변수 ,인스턴스 변수 값 쓰기 장려 안 함) -> naming mangling
# 타 클래스 __name 접근하지 않는 것이 원칙
class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0
        self._z = 0 ## high class에서 활용할 예정이니 protected variable 장려
        
a = SampleA()
a.x = 1
print('Ex 2 > x : {}'.format(a.x))
# print('Ex 2 > y : {}'.format(a.__y)) ## no attribute == private
print('Ex 2 > z : {}'.format(a._z))
print('Ex 2 > ', dir(a)) ## '_SampleA__y'
a._SampleA__y = 2
print('Ex 2 > y : {}'.format(a._SampleA__y)) ## private variable은 변형된 이름으로 되어 있어, 이렇게 수정은 가능

##### Ex 3 : 접근지정자 Ex 2 처럼 attribute의 직접 수정은 장려하지 않는 방식, method를 활용하여 변경 장려 (중요)
# method 활용 getter, setter
class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0

    def get_y(self):
        return self.__y
    
    def set_y(self, value):
        self.__y = value
        
b = SampleB()
b.x = 1
b.set_y(2)
print('Ex 3 > x : {}'.format(b.x))
print('Ex 3 > y : {}'.format(b.get_y()))
## 변수 수정에 일관성 및 가동성 상승
print('Ex 3 > ', dir(b))