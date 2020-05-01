class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        tmp = self.current
        self.current += 1

        if tmp < self.stop:
            return self.getTimeFormat(tmp)
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.getTimeFormat(self.start + index)

    def getTimeFormat(self, time):
        second = time
        minute = second // 60
        second %= 60
        hour = minute // 60
        minute %= 60
        hour %= 24
        return "{0:02d}:{1:02d}:{2:02d}".format(hour, minute, second)

start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')