def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise # 현재 예외를 다시 발생시킨다.

try:
    three_multiple()
except Exception as e:
    print('예외가 발생하였습니다.', e)