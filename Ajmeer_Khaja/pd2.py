import pandas as pd
print('the file is')
print(pd.__file__)

# csvfile = 'spcsv.csv'

# csvdata = pd.read_csv(csvfile)
# # print(csvdata)


# ##print entire dataframe 

# # print(csvdata.to_string())

# # print(pd.options.display.max_rows)

# # ##imcreaing the display of max rows
# # pd.options.display.max_rows=9999
# # print(pd.options.display.max_rows)

# jsondataindict = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# print(pd.DataFrame(jsondataindict))

# print(csvdata.head(10))
# print(csvdata.tail(10))

import sys
print(sys.executable)
print(sys.path)
# print(csvdata.info())