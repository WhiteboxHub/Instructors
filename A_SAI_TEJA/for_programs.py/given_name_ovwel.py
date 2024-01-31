# find the given name is ovwel or not
name = input("enter the name:- ")
ovwel = ['a', 'e', 'i', 'o', 'u']
for char in name:
    if char in ovwel:
        print(char,'is a ovwel')
    else:
        print(char,'is a consonant')
