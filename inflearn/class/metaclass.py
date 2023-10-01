"""
class of class : type, 모든 클래스의 메타
type, meta class : 클래스를 만드는 역할로 의도하는 대로 클래스 커스텀, 프레임워크 작성 시 필수, 동적 생성 가능
custom meta class : 검증 클래스 생성이 가능, 프레임워크를 위한 엄격한 class 사용이 요구 가능, 메소드 오버라이드 요구 가능
"""

##### Ex 1 - Type 예제
# class SampleA(object):
## type은 type이 metaclass
class SampleA(): ## class == object
    pass

obj1 = SampleA() ## 인스턴스 : 변수에 할당 가능, 복사 가능, 새로운 속성 추가 가능, 함수 인자로 활용 가능
# obj2 = SampleA() ## type metaclass
print("Ex 1 > ", obj1.__class__)
print('Ex 1 > ', type(obj1))
print('Ex 1 > ', obj1.__class__ is type(obj1))
print("Ex 1 > ", obj1.__class__.__class__) ## <class 'type'>
print("Ex 1 > ", obj1.__class__.__class__ is type(obj1).__class__) ## <class 'type'>
print("Ex 1 > ", type.__class__)
print("*" * 100)

##### Ex 2 - type meta 예제
## int, dict 등 모든 파이썬의 자료형은 모두 class
n = 10
d = {'a' : 10, 'b' : 20}

class SampleB():
    pass

obj2 = SampleB()

for o in (n, d, obj2):
    print('Ex 2 > {} {} {} {}'.format(o, type(o), type(o) is o.__class__, o.__class__.__class__))
print("*" * 100)
 
for t in (int, float, list, tuple, dict):
    print('Ex 2 > {} {} {} {}'.format(t, type(t), type(t) is t.__class__, t.__class__.__class__))