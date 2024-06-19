import pandas as pd
import os

print('the os cwd is')
print(os.getcwd())


mydata = {
    'cars':['lambo','pagani','ferari','BMW','mercedice','audi']
    ,'topspeed':[340,320,300,318,281,298]
    ,'BasePrice':['400K $','3.2M $','250K $','140K $','140k $','160K $']
}

myvar = pd.DataFrame(mydata)
print(myvar)
print(pd.__version__)

print(pd.Series(mydata))


ar = [1,2,3,4,5,6]
print(pd.Series(ar))

r = pd.Series(ar,index=['a','b','c','d','e','f'])

print(r)

calories = {"day1": 420, "day2": 380, "day3": 390}

print(calories)


mycal = pd.Series(calories,index=['day1','day2'])
print(mycal)
# spwap = {v:k for k,v in calories.items()}
# print(spwap)

cal_data = {
    "calories":[234,245,330,430,411,365]
    ,"duriation":[24,26,30,38,32,31]
}

print(f"the calories data is {cal_data}")

pdcal = pd.DataFrame(cal_data)
print(f"The Data Frame of Calories data is: \n {pdcal}")


print(pdcal.loc[[0,3,4,1]])


dindex = pd.DataFrame(cal_data,index=['D1',"D2",'D3',"D4","D5",'D6'])
print(dindex)


print(f"the value at Day3 is \n {dindex.loc['D3']}")

##reading a csv file in pandas
# csvfile = 'sp.csv'
csvfile = 'spcsv.csv'

csvdata = pd.read_csv(csvfile)
print(csvdata)
