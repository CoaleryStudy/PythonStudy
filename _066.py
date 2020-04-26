class Counter:
    def __init__(self, end):
        self.current = 0
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration

for i in Counter(3):
    print(i, end=' ')
print()

a, b, c, d, e = Counter(5)
print(a, b, c, d, e)