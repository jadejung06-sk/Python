"""
meta class
type inheritance : 객체가 인스턴스가 될 때, 내부적으로 호출되는 method를 활용
custom metaclass : 클래스 생성 가로채기(intercept), 클래스 수정(modify), 클래스 개선(기능 추가), 수정된 클래스 반환


"""
##### Ex 1 : 커스텀 메타클래스 생성 (Type 상속 X)
## 가져온 클래스에서 내가 필요한 부분만을 클래스로 만들어서 사용하는 경우에 활용

def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d
        
def cus_replace(self, old, new):
    while old in self: ## replace
        self[self.index(old)] = new

CustomList1 = type('CustomList1', (list, ), {'desc' : 'custom list1', 'cus_mul' : cus_mul, 'cus_replace': cus_replace})

c1 = CustomList1([1,2,3,4,5,6,7,8,9]) ## self == [1,2,3,4, ... , 9]
c1.cus_mul(1000)
c1.cus_replace(1000, 7777)

print('Ex 1 > ', c1 )
print('Ex 1 > ', c1.desc )
print('Ex 1 > ', dir(c1) )

##### Ex 2 : 커스텀 메타클래스 생성 (Type 상속 O)

# class MetaClassName(type):
    # def __new__(metacls, name, bases, namespace):
        
        
# new func > init func > call func 실행 순서
class CustomListMeta(type):
    ## 2 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print('__init__ >>> ', self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict) ## 넘겨주는 것
        
    ## 3 인스턴스 실행
    def __call__(self, *args, **kwargs):
       print('__call__ >>> ', self, *args, **kwargs)
       return super().__call__(*args, **kwargs)
        
    ## 1 클래스 인스턴스 생성 (메모리 초기화, 할당)    
    def __new__(metacls, name, bases, namespace):
        print('__new__ >>> ', metacls, name, bases, namespace)
        namespace['desc'] = 'CustomList2'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace
        
        return type.__new__(metacls, name, bases, namespace)
    
CustomList2 = CustomListMeta('CustomList2', (list, ), {})
c2 = CustomList2([1,2,3,4,5,6,7,8,9])
c2.cus_mul(1000)
c2.cus_replace(1000, 7777)

print('Ex2 > ', c2)
print('Ex 2 > ', c2.desc)
print('Ex 2 > ', CustomList2.__mro__) ## 상속 확인 : CustomList2 는 list를 상속, list는 object를 상속