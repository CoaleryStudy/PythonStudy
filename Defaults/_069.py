def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield total) # Yield data and Get data
            total += x
    except GeneratorExit: # if coroutine were stopped, GeneratorExit occured.
        print('\nCoroutine Stopped.')

co = sum_coroutine()
next(co)
# co.send(None)

for i in range(20):
    print(co.send(i), end=' ')

co.close() # Coroutine Stop.