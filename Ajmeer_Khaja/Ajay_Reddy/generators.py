# write a table by useing generators and take the information from the user
n=int(input("enter which table you want"))
def table(num):
    for i in range(1,11):
        yield f"{num} * {i} = {num*i}"
        i+=1
result = table(n)
for i in result:
 print(i)