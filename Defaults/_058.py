class Person:
    count = 0

    def __init__(self):
        Person.count += 1
    
    @classmethod
    def create(cls):
        return cls()

    @classmethod # 클래스 속성, 클래스 메서드에 접근가능.
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))

james = Person()
maria = Person()

newPerson = Person.create()

Person.print_count()