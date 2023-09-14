# Try this code and see what it prints:
# for i in range(5):
#     # what values does i equal as the loop runs
#     # 
#     print(2 * i)

# Homework #1 : Now write code to print the following
# 0
# 2
# 4
# 6

# for n in range(4):
#     print(2 * n)

# Try this code and see what it prints:
# for i in range(2, 5):
#     print(i)

# Homework #2: Now write code to print the following:
# 1
# 2
# 3
# 4
# 5
# 6

# for n in range (1, 7):
#     print (n)

# for r in range (6):
#     # first time through the loop, i = 0
#     # print 1 + r = 1 + 0 = 1
#     # 0, 1, 2, 3, 4, 5: 1 between each value
#     print(1 + r)


# Homework #3: rewrite the answer to h.w. #2 to print as follows
# 1 2 3 4 5 6

# for n in range(1, 7):
#     print(n, end=" ")

# tricky: Homework #4: using a loop and if statement, print the following
# 0
# 2
# 3
# 5
# 6
# 7

# not print the 1 and not print the 6
# for n in range(8):
#     # 0, 1, 2, 3, 4, 5, 6, 7
#     if n != 1 and n != 6:
#         print(n)

# Homework #5: here is a list
# adding to the list happens with my_list.append()
# this is just subscripting the list
my_list = [1, 2, 3, 4, 5]
# print(my_list[1])
# predict what happens when you run print(my_list[1]) and see if you are right

# Homework #6
# now write code using a for loop and my_list to print
# 1
# 2
# "aaa"
# 4
# "aaa"

# compound condition
# an 'and' or an 'or' in the condition


# == : comparison operator
# < : less than
# <= : less than or equal to

# in English: replace the 3 and the 5 with "aaa"
# in code: we are looking at one value at a time:
#    why does this mean we use 'or'?
for i in my_list:
    # i is 1: is condition true? no
    # i is 2: 
    # i is 3
    # i is 4
    # i is 5
    if i == 3 or i == 5:
        print("aaa")
    else:
        print(i)