def remove_duplicates(list):
    if not list:
        return 0
    k=0
    
    for i in range(0,len(list)):
        if list[i]!=list[i-1]:
            list[k]=list[i] 
            k+=1
            
    return k



list=[2,2,4,3,12,1,1,2]
new_list=remove_duplicates(list)

print(f"Output: {new_list}, nums = {list[:new_list]}")


