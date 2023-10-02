"""
Type(name - 이름, bases - 상속, dct - 속성, 메소드), dynamic metaclass

메타 클래스 
1. type으로 동적 클래스 생성 가능하다는 것이 가장 중요한 부분
2. 동적 생성한 메타클래스는 커스텀 메타클래스 생성 가능
3. 의도하는 방향으로 직접 클래스 생성에 관여할 수 있다는 장점
"""

##### Ex 1 - type 동적 클래스 생성 예제 : attribute
s1 = type('Sample1', (), {})
# == class Sample1(object): pass

print('Ex 1 - 1 > ', s1) ## <class '__main__.Sample1'>
print('Ex 1 - 1 > ', type(s1)) ## <class 'type'>
print('Ex 1 - 1 > ', s1.__base__) ## <class 'object'> 상속받는
print('Ex 1 - 1 > ', s1.__dict__) ## namespace
print('*' * 100)

class Parent1:
    pass
s2 = type('Sample2', (Parent1, ), dict(attr1 = 100, attr2 = 'hi')) ## 
# == class Sample2(Parent1): attr1 = 100 attr2 = 'hi'
### TypeError: type.__new__() argument 2 must be tuple, not type
## s2 = type('Sample2', (Parent1  ), dict(attr1 = 100, attr2 = 'hi'))

print('Ex 1 - 2 > ', s2) ## <class '__main__.Sample1'>
print('Ex 1 - 2 > ', type(s2)) ## <class 'type'>
print('Ex 1 - 2 > ', s2.__base__) ## <class 'object'> 상속받는
print('Ex 1 - 2 > ', s2.__dict__) ## namespace
print('Ex 1 - 2 > ', s2.attr1, s2.attr2)
print('*' * 100)

##### Ex 2 - type 동적 클래스 생성 예제 : method
class SampleEx:
    attr1 = 30
    attr2 = 100
    
    def add(self, m, n):
        return m + n
    
    def mul(self, m, n):
        return m * n
    
ex = SampleEx()

print('Ex 2 - 1 > ', ex.attr1, ex.attr2)
print('Ex 2 - 1 > ', ex.add(100, 200), ex.mul(100, 200))

print('*' * 100)

s3 = type('Sample3', (object, ), dict(attr1 = 300, attr2 = 1000, add = lambda x, y : x + y, mul = lambda x, y : x * y  ))
          ## ,{'attr1' : 30, 'attr2' : 100, 'add' : lambda x, y : x + y, 'mul' : lambda x, y : x * y  } )

print('Ex 2 - 2 > ', s3.attr1, s3.attr2)
print('Ex 2 - 2 > ', s3.add(1000, 2000), s3.mul(1000, 2000))