import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# arr = random.randint(80,130,size=(1,10))
# print(arr)
# sns.displot(arr,kind='kde')
# # plt.show()
# sns.histplot(arr)

# # plt.show()

# sns.kdeplot(arr)
# # plt.show()

# x = random.normal(size=(2,3))
# print(x)


# y = random.normal(loc=1,scale=2,size=(3,3))
# print(y)

# print(np.mean(y))

rdata = random.normal(size=1000);
print(rdata)
# sns.histplot(rdata)
# plt.show()

# sns.kdeplot(rdata)
sns.displot(rdata)

plt.show()