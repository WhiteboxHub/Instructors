'''def swap_case(s):
    swap=''
    for char in s:
        if char.islower():
            swap+=char.upper()
            print(swap)
        elif char.isupper():
            swap+=char.lower()
        else:
            swap += char
    return swap
    
re=swap_case('sAi tEJAa')
print(re)'''


def unique_elements(list1, list2):
    unique_list = []

    for item in list1 + list2:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(unique_elements(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7]



def unique_elements(list1,list2):
    unique_list=[]
    for item in list1+list2:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
