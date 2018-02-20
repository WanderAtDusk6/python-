class Myclass:
    name='sam'

    def sayHi(self):
        print('hello %s'%self.name)
        
mc = Myclass()
print(mc.name)
mc.name='lily'
mc.sayHi()
