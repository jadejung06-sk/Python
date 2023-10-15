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


##### Ex 2 - property 클래스 사용 property(fget = None, fset = None, fdel = None, doc = None)
class DescriptorEx2(object):
    def __init__(self, value):
        self._name = value
    
    def getVal(self):
        return "Get method called. -> self : {}, name : {}".format(self, self._name)
    
    def setVal(self, value):
        print('Set method called.')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('Name should be string.')
        
    def delVal(self):
        self._name = None
        
    name = property(getVal, setVal, delVal, 'property method example')
    
##
s2 = DescriptorEx2('Descriptor Test2')
print('Ex 2 > ', s2.name)
s2.name = 'Descrip Test2 Method.'
# s2.name = 10 ## TypeError: Name should be string.
print('Ex 2 > ', s2.name)
del s2.name
print('Ex 2 > ', DescriptorEx2.name.__doc__)