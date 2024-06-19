from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# x = random.binomial(n=100,p=0.5,size=1000)
# n = random.normal(loc=50,scale=5,size=1000)

# print(x)
# sns.displot(x,legend="binomial")
# sns.displot(n,legend='normal')
# plt.show()


# Sample data
x = np.random.binomial(n=10, p=0.5, size=1000)  # Binomial distribution
n = np.random.normal(loc=0, scale=1, size=1000)  # Normal distribution

# # Create a figure and a set of subplots
# fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# # Plot the first displot (binomial distribution)
# sns.distplot(x, kde=True, ax=axes[0])
# axes[0].set_title('Binomial Distribution')
# axes[0].set_xlabel('Values')
# axes[0].set_ylabel('Frequency')
# axes[0].legend(['Binomial'])

# # Plot the second displot (normal distribution)
# sns.distplot(n, kde=True, ax=axes[1])
# axes[1].set_title('Normal Distribution')
# axes[1].set_xlabel('Values')
# axes[1].set_ylabel('Frequency')
# axes[1].legend(['Normal'])

# # Adjust the layout
# plt.tight_layout()

#creaet a figure and a single subplot
# plt.figure(figsize=(10,16))
# sns.histplot(x,kde=True,color="blue",label="Binomial",alpha=0.5)
# sns.histplot(n,kde=True,color="red",label="normal",alpha=0.5)
# plt.title("overlapping Distribution")
# plt.xlabel('values')
# plt.ylabel('frequescy')
# plt.legend()


##create afigure for single subplot

plt.show()
sns.distplot(x,hist=False,label="binomial")
sns.distplot(n,hist=False,label='normal')
plt.show()