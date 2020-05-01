i = 1
while i < 11: # While 루프
    print("Hello", i)
    i += 1

res = 0
while True: # 무한 루프
    print("현재 값들의 합 : ", res)
    hi = int(input("값을 입력해주세요! : "))
    if hi == 0:
        break
    res += hi

py = "파이썬"
for s in py: # for 루프
    print(s)

for col in range(2, 10): # 구구단
    for row in range(1, 10):
        print(col, "×", row, "=", col * row)