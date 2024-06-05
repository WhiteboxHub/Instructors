a=[1,2,3,4,'sonu',1.22]
print(type(a))
print(a)
print(a[1])
print(a[0:3:2])
print(a[-1])

#methods

a.append('abc')  #adding at last in list
print(a)
a.extend([1,2,3,4,5,6]) #to add bulk data
print(a)
print(a.count(1))  # number repetition count
a.remove(2)  # to remove element
print(a)
a.pop(0) # to remove element by using index
print(a)
print(a.index(1))
a.insert(0,"kk")  # adding in preffered location
print(a)

#using for loop
for i in [1,2,3,4,'sonu',1.22]:
    print(i)