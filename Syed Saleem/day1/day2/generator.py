
#In this example, the generator function `my_generator` uses the `yield` keyword to return a sequence of three integers. The `for` loop then iterates over the generator and prints each integer.

##```python
def my_generator():
    for i in range(1,10):
        yield i
    
gen = my_generator()

for i in range(5):
    print(next(gen))  # 1

