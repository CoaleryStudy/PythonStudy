def trace1(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper

def trace2(func):
    def wrapper(a, b):
        r = func(a, b)
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))
        return r
    return wrapper

def trace3(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
        return r
    return wrapper

def trace4(x):
    def real_decorator(func):
        def wrapper(a, b):
            r = func(a, b)
            if r % 3 == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_decorator

@trace1
def hello():
    print('hello')

@trace2
def add(a, b):
    return a + b

@trace3
def get_max(*args):
    return max(args)

@trace3
def get_min(**kwargs):
    return min(kwargs.values())

@trace4(3)
def multiply(a, b):
    return a * b

hello()
add(32, 23)
print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))
print(multiply(4, 5))