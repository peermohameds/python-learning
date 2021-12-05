def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(is_leap_year(2000))
print(is_leap_year(1900))
print(is_leap_year(1996))
print(is_leap_year(1987))