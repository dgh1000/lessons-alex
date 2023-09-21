# playing with format string
# 
# Uncomment the following code and run it:

# s = "a phrase goes here"
# print(s)

# Question 1: What happens when you run this code?
# Are you clear on why it does that?

# Uncomment the following code and run it:

# x = 3
# print(x)

# Question 2: What happens when you run this code?
# Are you clear on why it does that?

# Uncomment the following code and run it:

x = 3
# s = f"The value of x is {x}"
# print(s)

# or you can do


# print(f"The value of x is {x}")

# Question 3: What happens when you run this code?

# A string with an f in front of it is called a format string.
# The special thing about it is that it can have curly braces
# inside. For example, notice the {x} in the above string.
# When the format string is evaluated, the value of x is
# inserted into the string. This is called string interpolation.

# Question 4:
# in your answer to this question, include the following line
# of code:
x = 3
# Write an assignment statement that assigns the
# string s to the string "The value of x is 3"
# using string interpolation (that is, the format string).
# You aren't allowed to use the value 3 in your answer.
# Then print s.

# Question 5:
# Uncomment the following code and run it:
# x = 3
# y = 4
# s = f"x plus y = {x + y}"
# print(s)

# What happens when you run this code?
# This demonstrates that you can put an expression inside
# the curly braces. The expression is evaluated and the
# result is inserted into the string.

# Create a format string that includes two expressions
# (things inside the curly braces) and three variables.

x = 1
y = 2
z = 3
# print(f"the combined numbers of x, y, and z are equal to {x + y + z}")

# print(f"the combined numbers of x and y are {x + y} but z is {z}")

# TRIPLE quotes strings
s = "A triple quoted string"
s2 = """This is a very long string. It's so long that it starts 
to run off the right edge of the screen we really don't want 
that because it makes it hard to read."""

room1_description = """You enter a room with a table and a chair.
There is a door to the north and a door to the west.
The light is dim. A fireplace glows eith embers."""

# print format string that incorporates the string name
name = "bob"
job = "at mcdonalds"
print(f"your name is {name}, you're an average man working {job}")
print("We can have a single quote inside a string. It's easy.")
# single quote: apostrophes: ', quote ": two different characters
# The man walked in the bank and said "Give me all your money!"
man = 'The man walked in the bank and said "Give me all your money!"'
# man = 'another kind of string' # in Python this is allowed
print(man)
