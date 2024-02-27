""" 
5 ways of importing modules
"""

import cal

# Using functions from the calculator module
result_add = cal.add(5, 12)
result_subtract = cal.subtract(8, 2)
result_multiply = cal.multiply(4, 6)
result_divide = cal.divide(10, 2)

print("Addition Result:", result_add)
print("Subtraction Result:", result_subtract)
print("Multiplication Result:", result_multiply)
print("Division Result:", result_divide)




import cal as cl

result_add = cl.add(12, 24)
result_subtract = cl.subtract(4, 6)
result_multiply = cl.multiply(5, 9)
result_divide = cl.divide(15, 3)

print("Addition Result:", result_add)
print("Subtraction Result:", result_subtract)
print("Multiplication Result:", result_multiply)
print("Division Result:", result_divide)







from cal import add

result_add = add(15, 32)
print("Addition Result:", result_add)







from cal import subtract as sub

result_subtract = sub(12,8)
print("Subtraction Result:", result_subtract)







from cal import *

result_add = add(23, 12)
result_subtract = subtract(8, 2)
result_multiply = multiply(4, 6)
result_divide = divide(10, 2)

print("Addition Result:", result_add)
print("Subtraction Result:", result_subtract)
print("Multiplication Result:", result_multiply)
print("Division Result:", result_divide)





#pre defined Modules

import datetime as dt

time_now = dt.datetime.now()
print(time_now)



import random

random_number = random.randint(1,100)
print(random_number)



print(dir(random))
print(dir(dt))
print(dir(cal))