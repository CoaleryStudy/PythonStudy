def countdown(n):
    cur = n + 1
    def inner_countdown():
        nonlocal cur
        cur -= 1
        return cur
    return inner_countdown

n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')