#---------exception
#-----------ex


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"The result of {a} / {b} is: {result}")
    finally:
        print("This block always executes, whether there's an exception or not.")

divide_numbers(10, 2) 

#-----------ex2

class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Error: Negative number {value} not allowed.")

def process_positive_number(number):
    try:
        if number < 0:
            raise NegativeNumberError(number)
        else:
            print(f"Processing positive number: {number}")
    except NegativeNumberError as e:
        print(e)

process_positive_number(-5)   


#--------------------ex3

class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Error: Negative number {value} not allowed.")

def process_positive_number(number):
    try:
        if number < 0:
            raise NegativeNumberError(number)
        else:
            print(f"Processing positive number: {number}")
    except NegativeNumberError as e:
        print(e)

process_positive_number(10)   

#----------ex4

def calculate_average(numbers):
    try:
        total = sum(numbers)
        average = total / len(numbers)
        print(f"The average is: {average}")
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

calculate_average([10, 20, 30, 40])