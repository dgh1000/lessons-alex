

# first we will not reverse a string

# line 4 is what kind of statement? assignment statement
# sets up the variable my_list with a value.
my_list = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"]
#           0    1    2    3    4    5    6    7    8    9    10 
# these are the indicies of the list
#  variables have values
s = "Hello World" # string
#    012345678910
# s = 5 # int (integer)
# s = 7.0 # floating point or in Python, "float"
# HOMEWORK: change the index to different values 
#   including different negative numbers
# i did lines 18-19 as the homework
# print(s[1]) 
# print(s[-1])
# values that have indices can be subscripted
# subscripting s: s[0], s[1]
# 
# HOMEWORK 9/6: review what values i takes on during the loop
# HOMEWORK 9/6: review: to get the letter we have to subscript
#          s by i: s[i]
# HOMEWORK 9/6: what values does i take on during the loop
for i in range(len(s)):
    # HOMEWORK: review difference between s[i] and i[s]
    #   and i and s
    print(s[i]) # subscripting s 

# i did lines 29-30 as the homework
print(i[s]) # this is an error, it cannot print i subscripted s because i isnt a value connected to s
print(s[i])
# doesn't seem like this makes much sense.
# this is clearly the very long way to do this.
# new_string = ""  # empty string
# new_string = new_string + "H"
# new_string = new_string + "e"
# new_string = new_string + "l"
# new_string = new_string + "l"
# new_string = new_string + "o"
# print(new_string)

s2 = "Hello world i have an announcement to make"
# HOMEWORK: change 
# line 44 (new_string = new_string + s2[i]) 
# to make new_string equal to
# s2 in reverse.
# Let me encourage you to experiment and try
# many different things.
# new_string = ""
# for i in range(len(s2)):
#     # what values does i take on during the loop
#     # 
#     new_string = new_string + s2[-i]
# print(new_string)

