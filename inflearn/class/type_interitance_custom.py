"""
meta class
type inheritance : 객체가 인스턴스가 될 때, 내부적으로 호출되는 method를 활용
custom metaclass


"""
##### Ex 1 : 커스텀 메타클래스 생성
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