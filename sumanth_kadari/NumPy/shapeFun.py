import numpy as np

#shape function()
a=[[10,20,30],[40,50,60]]   #2rows*3colums
a=np.shape(a)   
print(a)  

#reshape function()
a=[[10,20,30],[40,50,60]]  
a=np.reshape(a,(3,2))  #3rows*2colums
print(a)  

#-----------------zeros()------------------------------->
a=np.zeros((2,3),dtype=int)
print(a)

a=np.ones((3,2))
print(a)

#-----------Full()-------------------------->
a=np.full((2,3),5,dtype=int)
print(a)

#-------------eye()------------------------->
a=np.eye(3,2)
print(a)


#----------------Datatypes---------------->
a=np.array([10,20,30],dtype="U") #unicode str
print(a)


a=np.array([10,20,30,40],dtype="O")
print(a)

#Converting dtype on existing array 
a=np.array(["10","20","30"])
x=a.astype("i")
print(x)
print(x.dtype)

#--------copy()--------------------------------->
a=np.array([10,20,30])
c=a.copy()
c[1]=70
print(c)
print(a)


#-------------view()---------------------------->
a=np.array([40,50,70])
c=a.view()
c[1]=60
print(c)
print(a)