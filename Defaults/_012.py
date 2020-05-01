dict1 = {'하나':1, '둘':'two', '파이':3.14}
dict2 = dict({'하나':1, '둘':'two', '파이':3.14})
dict3 = dict([('하나', 1), ('둘', 'two'), ('파이', 3.14)])
dict4 = dict(하나=1, 둘='two', 파이=3.14)

print(dict1)
print(dict2)
print(dict3)
print(dict4)

dict5 = {'자바' : 70, '파이썬' : 80, 'C++' : 90}
print(dict5['자바'])
print(dict5.get('자바'))
print(dict5.get('HTML')) # Return None

dict5['HTML'] = 100
print(dict5)

del dict5['C++']
print(dict5)

dict5['자바'] = 100
print(dict5)

dict5.clear()
print(dict5)

dict5 = {'자바' : 70, '파이썬' : 80, 'C++' : 90}
print(dict5.keys())
print(dict5.values())
print(dict5.items())

print('자바' in dict5)
print('HTML' in dict5)