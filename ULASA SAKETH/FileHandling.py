#reading,writing,deleting,,creating of a file is called file handling.

'''
open
read/write
close
'''

'''
#read mode(it can only read data)

x=open('Test.txt',mode='r')
print(x.read())
x.close


'''

'''
#write mode(it can only write data)

x=open('Test.txt',mode='w')
x.write("hey")
x.close

'''

'''
#append mode(by using append the previos data wont be errased while write)

x=open('Test.txt',mode='a')
x.write("hi,how are you")
x.close

'''

'''
#read write mode(r+)
x=open('Test.txt',mode='r+')
print(x.read())
x.write("hey bro")
x.close

'''

#write read mode(w+)

x=open('Test.txt',mode='w+')
x.write("nice vision")
x.seek(0)
print(x.read())
x.close