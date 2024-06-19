#practicing python and numpy in notepad
#importing  the nummpy and math package along with asyncio

import numpy as np
import math
import asyncio
import time
import json
import threading
##declaring all the datatypes


my_int = 22
my_string = "Iam ajmeer khaja a passionate developer"
my_float = 11.23
my_list = ["apple","banana","kiwi"]
my_dict = {"name":"ajmeer khaja","age":22,"role":"software Intern"}
my_tuple = ("cat","dog","cow","rat","hen")


print(f"the integer is {my_int}")
print(f"the string is : {my_string}")
print(f"The value of float is : {my_float}")
print(f"The values in dict are : {my_dict}")

#using of loops

for i in range(len(my_string)):
	print(my_string[i])

count = 0


#using of while loop
# while count<len(my_dict):
# 	print( my_dict[count])


#creating function & classes


def my_fun_find_squre(number):
	return number*number

print(my_fun_find_squre(22))

#creating the employs class

class Emplooy:
	def __init__(self,name,age,empid):
		self.name = name
		self.age = age
		self.empid = empid
	def __str__(self):
		return f"The employ name is {self.name} is {self.age} year's old barring the employ id {self.empid}"

#inheritane
class HrDepartment(Emplooy):
	def __init__(self,name,age,empid,dep):
		super().__init__(name,age,empid)
		self.dep = dep
	def printDetails(self):
		print(f"The employ {self.name} working in Hr department ")



emp1 = Emplooy("ajmeer",22,1901)
emp2 = Emplooy("khaja",33,1892)
emp3 = HrDepartment("tom",43,1089,"hr Dept")

emp3.printDetails()

print(emp1)
print(emp2)



#using asyncio

async def my_asyncFun():
	return "This async function is executed"

async def main():
	print(await my_asyncFun())

asyncio.run(main())


#using of threads 

def fun1(a):
	print("Fun1 execution started")
	time.sleep(a)
	print("Fun1 is executed")
def fun2(a):
	print("Fun2 execution Started")
	time.sleep(a)
	print("Fun2 is executed")
def fun3(a):
	print("Fun3 execution started")
	time.sleep(a)
	print("Fun3 is executed")


fun1(1)
fun2(1)
fun3(1)

t1 = threading.Thread(target=fun1,args=[1])
t2 = threading.Thread(target=fun2,args=[2])
t3 = threading.Thread(target=fun3,args=[3])

t1.start()
t2.start()
t3.start()
#changing the json to dict or dict to json

new_my_dict = my_dict


dict_to_json = json.dumps(new_my_dict)

json_to_dict = json.loads(dict_to_json)


print(dict_to_json)
print(json_to_dict)


#the using of numpy


#declaring a numpy array


nparr = np.array(["tom","leo","Vikram","brad","murphy","Nolan","holand"],ndmin=2,dtype="S")


print(nparr)
print(nparr.dtype)
#prints the dimesion of the array
print(nparr.ndim)



copyarr = nparr.copy()


#in replication of a array every change in org array is automatically reflected onto the replicated array

replicatearr = nparr.view()

print(replicatearr)

nparr[0,1] = "tomHardy"
print(nparr)
	

print(nparr.base)

		