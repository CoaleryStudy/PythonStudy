n1, n2 = map(int, input().split())
a = {x for x in range(1, n1 + 1) if n1 % x == 0}
b = {x for x in range(1, n2 + 1) if n2 % x == 0}

divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)