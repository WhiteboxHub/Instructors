def mygen():
    n =1
    while n<20:
        yield n*n
        n +=1

value = mygen()
for i in value:
    print(i)



def newgen():
    engletters ="abcdefghijklmnopqrstuvwxyz"
    i=0
    while i< len(engletters):
        yield engletters[i]
        i+=1

neval = newgen()

for i in neval:
    print(i)
        