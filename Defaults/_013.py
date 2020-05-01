def hello():
    print('함수 시작')
    print('안녕하세요!')
    print('함수 끝')

def sum(a, b):
    print(a + b)

def returnSum(a, b):
    return a + b

hello()
hello()
hello()

sum(1, 2)
sum(3, 5)

print(returnSum(3, 4))
print(returnSum(7, 21))