class Hero:
    x = 123
    def __init__(self, skill1):
        self.q = skill1
        self.w = 'snowball'
        
    def hello(self):
        print('Hello!')
        
        
nunu = Hero('eat')
garen = Hero('strike')

print(nunu.x, nunu.q, nunu.w)
nunu.hello()
print(garen.x, garen.q, garen.w)
garen.hello()