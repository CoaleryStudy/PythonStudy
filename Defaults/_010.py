tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3

tuple3 = (1,) # 요소가 1개인 경우, 반점을 포함해야 튜플로 인식
tuple4 = (1)

print(tuple1)
print(tuple2)

print(tuple3)
print(tuple4)

packing = 10, "열", True # Packing
a, b, c = packing # Unpacking

print(packing)
print(10 in packing)
print("아홉" in packing)
print("아홉" not in packing)