try:
    c=10/0
    print(c)
except ZeroDivisionError as e:
    print(f"error:{e}")
except Exception as e:
    print(f"unexpected error:{e}")
else:
    print("no error")
finally:
    print("always")