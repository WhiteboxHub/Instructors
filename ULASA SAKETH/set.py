'''
{}
dont allow duplicates
no index,no order
do not allow mutable types as set elements
'''
ss={}
print(type(ss))
s={22,1,0,1,0,'hi','hello'}
print(type(s))
print(s)
#methods
s.add(27)                #it will add the data to the set
print(s)                  
s.update({28,12,14})     #it will add bulk data to the set
print(s)
s.remove(22)              # it will remove the give number
print(s) 
s.pop()                   # it will remove some number
print(s)
#operations
s1={1,2,3,4,6}
s2={4,5,6}
print(s1.union(s2))           #it will print both sets together with out duplicates
print(s1.intersection(s2))    #it will print common letters in both sets
print(s1.difference(s2))      #it wont give duplicate letters
print(s1.issuperset(s2))      #it will gives true if the numbers in set1 is same as s2
print(s2.issubset(s1))        #it will gives true if the numbers in set2 is same as set1

#for loop
for i in {1,2,3,4,5}:
    print(i)