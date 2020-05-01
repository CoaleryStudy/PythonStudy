def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

def calc_lambda():
    a = 3
    b = 5
    return lambda x: a * x + b

def calc_nonlocal():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total += + a * x + b
        print(total)
    return mul_add

c = calc()
print(c(1), c(2), c(3), c(4), c(5))

cl = calc_lambda()
print(cl(1), cl(2), cl(3), cl(4), cl(5))

cn = calc_nonlocal()
cn(1)
cn(2)
cn(3)