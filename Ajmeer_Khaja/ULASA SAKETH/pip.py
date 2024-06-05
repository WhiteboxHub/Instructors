#python package installer
#use of this library is - in a sentence, every first letter in the word changes to capital
#for that we will use 'hump' method

import camelcase
c=camelcase.CamelCase()
x="you can write anything you want"
y="if you write it correct you are good"
z=c.hump(x)
print(z)

