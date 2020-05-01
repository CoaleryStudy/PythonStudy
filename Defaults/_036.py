import string

line = ' ' + input() + ' '
for unit in string.punctuation:
    line = line.replace(unit, ' ')

print(line.count(' the '))