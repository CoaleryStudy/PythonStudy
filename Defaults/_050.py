plus_ten = lambda x: x + 10
print(plus_ten(1))

n1 = (lambda x: x + 5)(2)
print(n1)

l1 = list(map(lambda x: x + 10, [1, 2, 3]))
print(l1)

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l3 = list(map(lambda x: str(x) if x % 3 == 0 else x, l2))
print(l3)

l4 = [1, 2, 3, 4, 5]
l5 = [2, 4, 6, 8, 10]
l6 = list(map(lambda x, y: x * y, l4, l5))
print(l6)

l7 = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
l8 = list(filter(lambda x: x > 5 and x < 10, l7))
print(l8)

from functools import reduce

l9 = [1, 2, 3, 4, 5]
l10 = reduce(lambda x, y: x + y, l9)
print(l10)