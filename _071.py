def calc():
    result = 0
    while True:
        expression = (yield result)
        split = expression.split()
        lvalue = int(split[0])
        rvalue = int(split[2])
        if split[1] == '+':
            result = lvalue + rvalue
        elif split[1] == '-':
            result = lvalue - rvalue
        elif split[1] == '*':
            result = lvalue * rvalue
        elif split[1] == '/':
            result = lvalue / rvalue

expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()