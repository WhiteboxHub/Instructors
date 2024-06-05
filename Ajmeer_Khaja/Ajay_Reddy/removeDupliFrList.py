#remove duplicates from a list
def remove(lst):
    return list(set(lst))    
"""set removes all the duplicate values & after removing the duplicates LIST inbuilt method
will the set into list again the it will print"""
original = [1,2,3,4,2,4,5]
unique = remove(original)
print("original list is ",original)
print("unuique list is ",unique)