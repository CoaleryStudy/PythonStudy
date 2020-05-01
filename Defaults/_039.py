keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))
x2 = x.copy()

# Type 1
del x['delta']
x = {key : value for key, value in x.items() if value != 30}

# Type 2
x2 = {key : value for key, value in x2.items() if not (key == 'delta' or value == 30)}

print(x)
print(x2)