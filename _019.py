a = int(input('첫번째 정수를 입력해주세요! : '))
b = int(input('두번째 정수를 입력해주세요! : '))

try:
    result = a / b
except ZeroDivisionError: # 0으로 나누면
    print('0으로 나눌 수 없습니다!')
else: # 0으로 나누지 않았다면
    print(result)
finally: # 무조건 처리
    print('계산기 끝!')