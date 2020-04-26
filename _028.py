size = int(input())

# Type 1
for i in range(size):
    print(' ' * (size - i - 1), end = '')
    print('*' * (i * 2 + 1))

# Type 2
for i in range(size):
    for j in range(size - i - 1):
        print(' ', end = '')
    for j in range(i*2 + 1):
        print('*', end = '')
    print()