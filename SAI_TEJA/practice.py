def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

year = int(input('Enter the year: '))
print(is_leap(year))
