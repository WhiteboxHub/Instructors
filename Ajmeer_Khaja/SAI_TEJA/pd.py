import pandas as pd

"""mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)"""
# series...
import pandas as pd

print("Create a simple Pandas Series from a list:-")
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)


# create a labels..
print("create a labels")

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

#key/value objects as series....
print("create a simple pandas series from a dictionary:-")

calories = {"day1": 420, "day2": 380, "day3": 390} # the keys become the labels...
myvar = pd.Series(calories)
print(myvar)

myvar = pd.Series(calories, index = ["day1"])
print(myvar)

#data frames...

print("Create a simple Pandas DataFrame:-")

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 