a = {1, 2, 3, 4}
b = {1, 2, 3, 4}
c = {1, 2, 3, 4, 5}

d = {3, 4, 5, 6}
e = {6, 7, 8, 9}

print(a <= b) # Subset
print(a < b)
print(a < c)

print(a.isdisjoint(d))
print(a.isdisjoint(e))