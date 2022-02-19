import datetime


class Timer:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__time = datetime.time(hour, minute, second)

    def __str__(self):
        return f"{self.__time.strftime('%H:%M:%S')}"

    def next_second(self):
        self.__second += 1
        if self.__second >= 60:
            self.__second = self.__second % 60
            self.__minute += 1

        if self.__minute >= 60:
            self.__minute = self.__minute % 60
            self.__hour += 1

        if self.__hour >= 24:
            self.__hour = self.__hour % 24

        self.__time = datetime.time(self.__hour, self.__minute, self.__second)

    def prev_second(self):
        if self.__time.second == 0:
            if self.__time.minute == 0:
                if self.__time.hour == 0:
                    self.__hour = 24 - 1
                else:
                    self.__hour -= 1
                self.__minute = 60 - 1
            else:
                self.__minute -= 1
            self.__second = 60 - 1
        else:
            self.__second -= 1

        self.__time = datetime.time(self.__hour, self.__minute, self.__second)


timer = Timer(11, 0, 0)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)