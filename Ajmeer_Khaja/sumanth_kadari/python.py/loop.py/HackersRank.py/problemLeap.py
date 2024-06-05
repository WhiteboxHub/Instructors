year = int(input("Enter a year: "))

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Calling the is_leap function and printing the result
result = is_leap(year)
print(result)