import string

print(', python.'.lstrip(',.'))
print(', python.'.rstrip(',.'))
print(', python.'.strip(',.'))
print(', python.'.strip(string.punctuation + ' '))

print('python'.ljust(10))
print('python'.rjust(10))
print('python'.center(10))
print('35'.zfill(10))
print('3.5'.zfill(10))
print('hello'.zfill(10))
print('apple pineapple'.count('pl'))