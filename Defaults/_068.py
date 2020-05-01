def prime_number_generator(start, stop):
    for i in range(start, stop + 1):
        isPrime = True
        for j in range(2, int(i ** (0.5)) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            yield i

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')