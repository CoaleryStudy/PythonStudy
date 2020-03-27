class Dog:
    sound = "멍멍!" # Class Variable : 모든 인스턴스가 값을 공유한다. ( static ? )

    def __init__(self, name, age):
        self.name = name # Instance Variable : 인스턴스마다 서로 공유하지 않는다.
        self.age = age # Instance Variable

    def bark(self):
        print(self.name, ":", self.sound)

my_dog = Dog('dog1', 3)
your_dog = Dog('dog2', 4)

my_dog.bark()
your_dog.bark()
