#write a program to explane the value length arguements
def add(a,*b):
    c=a
    for i in b:
        c=c+i
    print("the sum of tuple is ",c)
    
add(1,3,5,4,6)