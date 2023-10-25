# Note: prerequisite for this lesson is list concatenation
# or lists/list-plus-01.py


my_list = [6, 1, -2, 3, 10, 13]
#

# Here is a demonstration of indexing or subscripting the list: (please
# write down the words indexing and subscripting to help you remember them)

# EXAMPLE A:

# Uncomment and run this code. Before you
# run it, predict what it will do.
# print(my_list[0])

# Question 1: 
# Explain in your own words what the code on line 8 does.

# Answer: it only processes the first value on the list instead of the whole list

# Question 2:
# Which of the values on line 14 is the "subscript" or "index"?

# answer: [] is the subscript, and 0 is the index

# Question 3:
# What "syntax" is used to subscript a list? In other words, 
# what characters are used and where do they go?

# Answer: my_list is the list, and to subscript the list you must print my_list followed by [0] or any other number

# Question 4:
# Write a line of code that will print the value 10 from the list.
# Figure what index you need, and then write the code.

# Answer:
# print(my_list[4])

# EXAMPLE B:

# Now we will address the topic of what you need to do to print 
# several items in a row from the list. You can start like this:
# Uncomment this code and run it. First predict what it will do.

# print(my_list[3])
# print(my_list[4])
# print(my_list[5])

# Question 5:
# Modify the code on lines 28 through 30 to print the values
# 3, 10, and 13 from the list.

# EXAMPLE C:

# Uncomment the following code and run it. First see if
# you can predict what it will do. You may not remember 
# it or perhaps we haven't done it before.

# print(my_list[3:6])

# Question 6:
# Explain in your own words what the code on line 48 does.

# Answer: it prints a chain of the selected values that are subscripted within the list

# EXPLANATION
# This syntax is called "slicing" a list. It is a way to
# get a section of a list. The first number is the starting
# index and the second number is the ending index. The
# ending index is not included in the slice. So in this
# example, the slice starts at index 0 and ends at index 2.
# The value at index 3 is not included.

# Question 7:
# What is different between the values printed in EXAMPLE B
# and the values printed in EXAMPLE C?

# Answer: example B showcases 3 seperate lines of code that prints one part of the list, while example C showcases 1 line that can achieve the same goal

# Question 8:
# Modify the code on line 60 to print the values 3, 10, and 13.
# What's the last index you need to include? What should the 
# second number be in the slice?

# Answer: the last value has an index of 5, and the second number of the slice is 1 greater

# EXAMPLE D:

# Uncomment the following code and run it. First see if you
# can predict what it will do. Note this involves list
# concatenation. We did this in lists/list-plus-01.py

# print(my_list[0:2] + my_list[3:5])

# Question 9:
# Explain in your own words what the code on line 78 does. 

# Answer: it combines the two variables into one

# Question 10:
# Modify the code on line 78 to print the list
# [6, 1, 3, 10]

# To review, Here is a copy of the line above that assigns 
# my_list:
# my_list = [6, 1, -2, 3, 10, 13]
