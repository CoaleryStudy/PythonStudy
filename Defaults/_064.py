class NotThreeMultipleError(Exception):
    def __init__(self, msg='3의 배수가 아닙니다.'):
        super().__init__(msg)

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print('예외가 발생하였습니다.', e)

three_multiple()