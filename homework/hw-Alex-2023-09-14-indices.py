

# Uncomment the following code. You'll use it in every problem
# below.
# part of a larger program like a game
# we need to account for the fact that 
# s1 may be various lengths. s1 is the player's name
s1 = "Nikki is cute"

# question #1. 

# Now write code that prints every other letter in s1. Use
# the 3-parameter form of range() to do this.

# Answer:
# for i in range(0,len(s1),2):
#     # using i as the index
#     # and we subscript s1 with i

#     print(s1[i])

# question #2.

# Write code that prints the first and last letters in s1. You
# won't use range() for this. You'll just subscript s1 (using
# square brackets) to get the first and last letters.

# What are loops good for? Loops do something multiple times
# without you having to write the same code over and over.
# When we don't know how many times it might loop. Number 
# of times might depend on user input, or the length of a
# string, or the number of elements in a list.

# How many times do we need to run the code? twice. 
# Therefore we don't need a loop. We can just write the code
# twice. 

# Answer:
# for i in s1[0], s1[-1]:
#     print(i)

print(s1[0])
print(s1[-1])
# question #3.

# Uncomment the following line
s2 = "hello there Mr. Doodle"

# Now Write code that prints every third letter of the string.
# Use range() to do this.

# Answer:
for i in range(0, len(s2), 3):
    print(s2[i])