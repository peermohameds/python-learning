class WeekDayError(Exception):
    pass


class Weeker:
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in Weeker.day_names:
            raise WeekDayError
        self.__day = day
    # Write code here
    #

    def __str__(self):
        return self.__day

    def add_days(self, n):
        index = (Weeker.day_names.index(self.__day) + n) % 7
        self.__day = Weeker.day_names[index]

    def subtract_days(self, n):
        index = Weeker.day_names.index(self.__day) - 1 - (n % 7)
        print(index)
        self.__day = Weeker.day_names[index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(7)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")