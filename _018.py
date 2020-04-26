f = open('_018.txt', mode='r')
file_lines = f.readlines()
print(file_lines)
f.close()

f2 = open('_018.txt', mode='a')
f2.write('\nHello!')
f2.close()

with open('_018.txt', 'r') as f3:
    file_data = f3.read()
    print(file_data)