

my_list = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"]
#           0    1    2    3    4    5    6    7    8    9    10 
s = "Hello World" # string
#    0123456789T

# HOMEWORK: review subscripting. subscripting involves brackets []
#   has to do with picking one item out of a list or one 
#   character out of a string
#   Try with and without the subscript.
# print(my_list[0])
#       ^^^^^^^     when subscripting what is this part? (see line 16 **)
#              ^^^  what is this part
# HOMEWORK: memorize meaning of index: we pick based on the
#           index
# (**) the part before the square brackets:
#      a list, a string, a variable containing a list or a string
#      What's special about them is they can contain multiple 
#      items. And subscripting picks out one of them. 
# HOMEWORK: try the following and verify they are all errors
# print([0]my_list)
# print(0[my_list])
# print([my_list]0)


# HOMEWORK : review what values i takes on during the loop
# len(s) is 11. numbers that actually come out when we run
#  this are 0 through 10: which is a total of 11 numbers
# for i in range(len(s)): # loop is in this form
#     print(s[i]) # adds a newline, or with end="" doesn't add a newline

# s = "Hello World"
#   H   e   l   l   o       W   o   r   l   d
# -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
#  11 numbers: same as the number of numbers from 1 to 11
#  same number of numbers as 0 through 10
#        0   1   2   3   4   5   6   7   8   9   10
# s[i]   H   e   l   l   0       w   o   r   l   d
# -i     0  -1  -2  -3  -4  -5  -6  -7  -8  -9  -10
# s[-i]  H   D   l   r   o   w       o   l   l   e
# 2*i    0   2   4   6   8   10  12  14  16  18  20
# s[2*i] H   l   o   w   r   d   these do not exist
s2 = "Hello world i have an announcement to make"
# HOMEWORK: change 
# line 44 (new_string = new_string + s2[i]) 
# to make new_string equal to
# s2 in reverse.
# Let me encourage you to experiment and try
# many different things.
new_string = ""
# i: 1   2   3   4   5   6   7   8   9  10  11
for i in range(1, len(s)+1):
    # 
    # what values does i take on during the loop
    # 
    new_string = new_string + s[-i]
print(new_string)

# for i in range(0, 11, 2):
    