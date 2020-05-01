class Person:
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print('Hello,', self.name)

p = Person('Coalery')
p.sayHello()

print(isinstance(p, Person))