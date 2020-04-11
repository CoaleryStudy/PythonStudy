dict_comprehension = { key : 0 for key in ['a', 'b', 'c', 'd']}
a = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

print(a)
print(dict_comprehension)

print({value: key for key, value in a.items()})
print({value: key for key, value in dict_comprehension.items()}) # 키 중복으로 마지막만 저장됨.

a = {key: value for key, value in a.items() if value != 20}
print(a)