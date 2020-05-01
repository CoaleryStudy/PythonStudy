set1 = {1, 2, 3}
set2 = set("Python")
set3 = set("Hello")

print(set1)
print(set2)
print(set3)

set4 = {} # 중괄호만 있는경우, 딕셔너리 타입으로 선언된다.
set5 = set()

print(type(set4))
print(type(set5))

set6 = {1, 2, 3, 4, 5}
set7 = set((1, 3, 5, 7, 9))

print(set6 & set7)
print(set6 | set7)
print(set6 - set7)
print(set6 ^ set7)