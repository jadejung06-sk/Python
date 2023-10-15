"""
descriptor : get, set - low level
1. 객체에서 서로 다른 객체를 속성값으로 갖음
2. read, write, delete 등 미리 정의
3. data descriptor(set, delete), non-data descriptor(get)
4. 읽기 전용 객체 생성에서의 장점, 클래스를 의도하는 방향으로 생성 가능
5. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
6. Property와 달리 reuse
7. ORM Framework 사용에 주로 쓰임

property : annotation - high level


"""

##### Ex 1 - descriptor
import os

class DirectoryFileCount:
    def __get__(self, obj, objtype= None): ## obj == class
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))

class DirectoryPath: ## obj
    ## Descriptor instance
    size = DirectoryFileCount()
    
    def __init__(self, dirname):
        self.dirname = dirname

s = DirectoryPath('./')
g = DirectoryPath('../')
s.size ## print()
print(s.size) ## return 37 len()
g.size ## print()
print(g.size) ## return 54 len()

print('Ex 1 > ',dir(DirectoryPath))
print('Ex 1 > ',DirectoryPath.__dict__) ## namespace
print('Ex 1 > ',dir(s)) 
print('Ex 1 > ',s.__dict__) ## namespace


##### Ex 2 - descriptor - logging class