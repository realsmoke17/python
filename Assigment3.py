# Student name: Makwarela F 
# Student no:  230384274
# Date:  30/09/2024
# Assignment 3: Python 

#Problem 1

# Given string
s = 'fullstackslp'

# 'f' 
print(s[0])

# 'p' 
print(s[-1])

# 'stack'
print(s[4:9])

# 'slp'
print(s[-3:])

# 'cks'
print(s[7:10])

# Bonus: 
print(s[::-1])

# Problem 2

# d1: Grab 'hello' from the simple dictionary
d1 = {'simple_key': 'hello'}
print(d1['simple_key'])

# d2: Grab 'hello' from a nested dictionary
d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])

# d3: Grab 'hello' from a deeply nested structure
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

# Problem 4

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
unique_values = set(mylist)
print(unique_values)


# problem 5

age = 45
name = "Kyle"

# Using print formatting to display the sentence
print(f"Hello my dog's name is {name} and he looks {age} years old")

