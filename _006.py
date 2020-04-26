i = "파이썬 "
j = "문자열"

print(i + j)
print(i * 3)

korean = "가나다라마바사아자차카타파하"
print(korean[0])
print(korean[6])
print(korean[-1])
print(korean[-2])
print(len(korean))

print(korean[4:7])
print(korean[:4])
print(korean[4:])

print(korean.count('다'))

print(korean.find('자'))
print(korean.index('자'))

print(korean.find('핣'))
# print(korean.index('핣')) -> ValueError!

py = "Python"
print(py.upper())
print(py.lower())
print(py.replace("P", "A"))

stuff = "apple banana circle dinosaur elephant"
print(stuff.split(' '))
print(stuff.split())