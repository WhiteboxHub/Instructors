#creating a list
'''a = [1,3,4,5,6,7,888,]
print(len(a))    #find length
print(type(a))  ''' #find datatype

#append
'''a=[1,3,4,5,6,77,'sumanth',True]
a.append(7)
print(a)'''

#extend
'''a = [23,4,6,7,8,9,'bunny',True]
a.extend([12,45])
print(a)'''

#insert
'''a=[1,3,3,4,5,'sumanth']
a.insert(1,'bunny')  #inserting in index number
print(a)'''

#count
'''a=[1,2,1,2,3,3,'sumanth',False]
print(a.count(1))'''

#pop
'''a=[12,23,1,2,3,'sumanth']
a.pop(2)
print(a)'''

#sorting
'''a=[12,2,3,1,55,7,99,12,]
a.sort()
print(a)'''

#using for loop in a list
'''a=[1,1,22,33,[66,77,10],55,90,'sumanth',True]
for i in a:
    print(i)'''
 
 #joint two lists
list1 = [1,2,3,4]
list2 = ['a','b','c','d']
for x in list1:
    list2.append(x)
print(list2)
