def divide_numbers(a, b):
    try:
        result = a / b
        print("Division result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Unsupported operand type(s).")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("This block is always executed, regardless of whether an exception occurred or not.")


divide_numbers(10, 2)  
divide_numbers(10, 0)  
divide_numbers(10, '2')











try:
    file = open("example.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("Error: File not found!")
except IOError:
    print("Error: Could not read the file!")
























