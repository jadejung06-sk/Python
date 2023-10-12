"""
descriptor : 
1. 객체에서 서로 다른 객체를 속성값으로 갖음
2. read, write, delete 등 미리 정의
3. data descriptor(set, delete), non-data descriptor(get)
4. 읽기 전용 객체 생성에서의 장점, 클래스를 의도하는 방향으로 생성 가능

set
get
del
property

"""

##### Ex 1 - basic descriptor
class DescriptorEx1(object):
    def __init__(self, name = 'Default'):
        self.name = name
        
    def __get__(self, obj, objtype):
        return 'Get method called. -> self : {}, obj : {}, objtype : {}, name : {}'.format(self, obj, objtype, self.name)
    
    def __set__(self, obj, name):
        print('Set method called.')
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Name should be string.')
        
    def __delete__(self, obj):
        print('Delete method called.')
        self.name = None
        
class Sample1(object):
    name = DescriptorEx1()
    
s1 = Sample1()
s1.name = 'Descriptor Test1'
# s1.name = 10 """   raise TypeError('Name should be string.') TypeError: Name should be string."""
print('Ex 1 > ', s1.name)
del s1.name
print('Ex 1 > ', s1.name)
print("*" * 100)


##### Ex 1 - property 클래스 사용