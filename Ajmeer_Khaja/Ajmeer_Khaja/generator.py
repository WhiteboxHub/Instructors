def mygen():
    n =1
    while n<20:
        yield n*n
        n +=1

value = mygen()
for i in value:
    print(i)



def newgen():
    strlen = 10;
    