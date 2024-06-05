A=(1,2,3,4,5,6)
B=(1,2,3,4,5,6)
print(type(A))
print(A)
print(len(A))  # it will give lenght of the tuple
print(A[1])
print(A[-1])
print(A[0:3])
print(A[-2:-1])

if 1 in A:
    print("hi")
for i in A:
    print(i)
print(min(A))  # it will display minimum number
print(max(A))  # it will display maximum number
print(sum(A))  # it will give the sum of number
print(A+B)     # it will add both tuple
print(A is B)  # if A is same as B
