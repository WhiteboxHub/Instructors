import pytest
import math

'''def func(x):
    return x+5

def test_func():
    assert func(3)==8'''

#first test case
def test_firstCase():           #in pytest, it is manditory to write 'test' keyword at function name to recognise it is a test case
    num=64                      #creating a variable and assigning a value
    assert math.sqrt(num)==8    #assert is used t check or compare

#second test case
def test_square():
    num=6
    assert num*num == 36

#third test case
def test_name():
    name="saketh"
    assert "th" in name