import re
a = 'my name is sai, my age is 23'
b=re.findall('23$',a)                                                       # meta characters [], ^, $, ., |, ?, *, +, {}, ()
print(b)