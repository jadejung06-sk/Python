"""
Method Overriding
overriding : 
1) 서브클래스에서 슈퍼클래스 호출 후 사용
2) 매소드 재 정의 후 사용 가능
3) 부모클래스의 메소드를 추상화 후 사용가능(구조적 접근)
4) 확장 가능, 다형성 (다양한 방식으로 동작)
5) 가독성 향상으로 오류 가능성 감소하고 메소드 이름을 절약, 유지보수성 향상

OOP
다형성
"""


##### Ex 1 Parent Class
## 기본 overriding 예제

class ParentEx1():
    def __init__(self):
        self.value = 5
        
    def get_value(self):
        return self.value
      
    
class ChildEx1(ParentEx1):
    pass

c1 = ChildEx1()
p1 = ParentEx1()
### 자식 클래스에서 부모 클래스 메소드 호출
print("Ex 1 > ", c1.get_value())

### c1 자식 클래스의 모든 속성 출력
print("Ex 1 > ", dir(c1)) ## , 'get_value', 'value']

### 부모 & 자식 모든 속성 출력
print("Ex 1 > ", dir(ParentEx1))
print("Ex 1 > ", dir(ChildEx1))
print("*" * 100)

### 네임스페이스 내의 영역에서의 모든 속성 출력, 인스턴스가 될 때 담긴다는 의미
print('Ex 1 > ', ParentEx1.__dict__) ## '__init__': <function ParentEx1.__init__ at 0x000001DBFD9ADCF0>, 'get_value': <function ParentEx1.get_value at 0x000001DBFD9ADC60>, '__dict__': <attribute '__dict__' of 'ParentEx1' objects>, '__weakref__': <attribute '__weakref__' of 'ParentEx1' objects>,
print('Ex 1 > ', ChildEx1.__dict__) ## Ex 1 >  {'__module__': '__main__', '__doc__': None}

##### Ex 2 
## 기본 overriding 메소드 재정의 예제

class ParentEx2():
    def __init__(self):
        self.value = 5
        
    def get_value(self):
        return self.value
      
    
class ChildEx2(ParentEx2):
    def get_value(self):
        return self.value * 10
    
p2 = ParentEx2()    
c2 = ChildEx2()

## 동일한 이름의 자식 메소드 재정의 후 호출
print("Ex 2 > ", c2.get_value())
print("Ex 2 > ", p2.get_value())

##### Ex 3
## overridng 다형성 예제
import datetime

class Logger(object):
    def log(self, msg):
        print(msg)
        
        
class TimestampLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts = datetime.datetime.now(), msg = msg)
        ### same methods
        # super().log(message)
        super(TimestampLogger, self).log(message)
        
        
class DateLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts = datetime.datetime.now().strftime("%Y-%m-%d"), msg = msg)
        ### same methods
        # super().log(message)
        super(DateLogger, self).log(message)
        
        
l = Logger()
t = TimestampLogger()
d = DateLogger()

print("Ex 3 > ", l.log('Called logger.'))
print("Ex 3 > ", t.log('Called timestamp logger.'))
print("Ex 3 > ", d.log('Called date logger.'))

l.log('test1')
t.log('test2')
d.log('test3')