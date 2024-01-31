#generators are like functions which contains yield keyword

def fun():
    return 1
    return 2
    return 3 
print(fun())


'''
def fun():
    for i in range(10):
        yield i
result = fun()
for j in result:
    print(j) 
'''