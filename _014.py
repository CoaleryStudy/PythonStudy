def sub(a, b):
    print(a - b)

def total(a, b = 5, c = 10):
    print(a + b + c)

def add(*params):
    print(params)
    total = 0
    for p in params:
        total += p
    return total

def print_map(**dicts):
    for item in dicts.items():
        print(item)

def arith(a, b):
    add = a + b
    sub = a - b
    return add, sub

sub(1, 2)
sub(b=1, a=2)

total(3)
total(1, 2)
total(1, 2, 3)

print(add(1, 2, 3, 4, 5, 6))
print(add(2, 4, 5))

print_map(하나=1)
print_map(one=1 , two=2)
print_map(하나=1, 둘=2, 셋=3)

a, b = arith(5, 2)
print(a, b)

print((lambda a, b: a + b)(1, 2))