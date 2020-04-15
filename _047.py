def personal_info(name, age, address):
    print('이름:', name)
    print('나이:', age)
    print('주소:', address)

def personal_info2(**kwargs):
    if 'name' in kwargs:
        print('name:', kwargs['name'])
    if 'age' in kwargs:
        print('age:', kwargs['age'])
    if 'address' in kwargs:
        print('address:', kwargs['address'])
    if 'type' in kwargs:
        print('type:', kwargs['type'])

x = {'name':'홍길동', 'age':30, 'address':'부산'}
personal_info(**x)

personal_info2(name='홍길동', age=30, address='부산')
personal_info2(name='홍길동', age=30, address='부산', type='사람')