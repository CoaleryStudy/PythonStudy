print('Hello, {0}'.format('world!'))
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.7))

print('{0} {0} {1} {1}'.format('Python', 'Script'))
print('Hello, {} {} {}'.format('Python', 'Script', 3.7))

print('Hello, {language} {version}'.format(language = 'Python', version = 3.7))

language = 'Python'
version = 3.7
print(f'Hello, {language} {version}')

print('{0:<10}'.format('python'))
print('{0:>10}'.format('python'))

print('{0:03d}'.format(35))
print('{0:08.2f}'.format(150.3))

print('{0:,}'.format(1493500))