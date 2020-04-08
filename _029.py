a1, a2 = map(int, input().split())

# Type 1
for i in range(a1, a2 + 1):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)

# Type 2
for i in range(a1, a2 + 1):
    res = ''
    if i % 5 == 0:
        res += 'Fizz'
    if i % 7 == 0:
        res += 'Buzz'
    if not res:
        res = i
    print(res)

# Type 3
for i in range(a1, a2 + 1):
    res = 'Fizz' * (i % 5 == 0) + 'Buzz' * (i % 7 == 0)
    if not res:
        res = i
    print(res)