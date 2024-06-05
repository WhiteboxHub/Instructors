"""
Regular expressions (regex) in Python are a powerful tool for pattern matching and text manipulation. 
Fython provides the re module for working with regular expressions. Here's a basic overview of how you can use regex in Cython:

1)Import the re Module:
Start by importing the re module in your Python script or interactive session:
==import re

2)Basic Patterns:

>>re.search(pattern, string): Search for a pattern in a string.
>>re.match(pattern, string): Match the pattern only at the beginning of the string.
>>re.fullmatch(pattern, string): Match the entire string against the pattern
    
    
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall     Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
    """
    
import re

pattern=r"[A-Z]+ython"
text="""Regular expressions (regex) in Python are a powerful tool for pattern matching and text manipulation. 
Fython provides the re module for working with regular expressions. Here's a basic overview of how you can use regex in Cython:


"""
print(re.findall(pattern,text))
print(re.search(pattern,text).span())
print(re.split(pattern,text))



#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re

def is_valid_string(input_string):
    # Define the pattern for alphanumeric characters
    pattern = re.compile(r'^[a-z0-9]+$')

    # Use the pattern to check if the string matches
    if pattern.match(input_string):
        return True
    else:
        return False

# Example usage:
input_str = input("Enter a string: ")

if is_valid_string(input_str):
    print("The string contains only a-z, A-Z, and 0-9.")
else:
    print("The string contains other characters.")







def correct_string(input_str):
    
    pattern=re.compile(r"^[a-z0-9A-Z]+$")
    
    if re.match(pattern,input_str):
        return True
    else:
        return False



in_str=input("enter the string :")
if correct_string(in_str):
    print(" string according to the patern ")
    
else:
    print("the string does not match with the pattern")




