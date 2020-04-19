class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    """
    @staticmethod
    def is_time_valid(time_string):
        time_split = time_string.split(':')

        if len(time_split) != 3:
            return False
        
        raw_hour = time_split[0]
        raw_minute = time_split[1]
        raw_second = time_split[2]

        if not (isinstance(int, raw_hour) and isinstance(int, raw_minute) and isinstance(int, raw_second)):
            return False

        hour = int(raw_hour)
        minute = int(raw_minute)
        second = int(raw_second)

        return 0 <= hour <= 24 and 0 <= minute <= 59 and 0 <= second <= 60
    
    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return cls(hour, minute, second)
    """ # Type 1

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour <= 24 and minute <= 59 and second <= 60

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return cls(hour, minute, second)
    # Type 2
    
time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')