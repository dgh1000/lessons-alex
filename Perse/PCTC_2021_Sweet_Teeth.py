# Amelie:6 Bakshi:7 Chloe:4
# A. has 6, eats 3, passs remainder 3 to Bakshi
# B. has 10, eats 5, passes 5 to Chloe
# C. has 9, eats 4, passes 5 to Amelie
# 3,10,4
# 3,5,9
# 8,6,4

A = int(input())
B = int(input())
C = int(input())

# consider the case A=1 and B=1
A_eats = A // 2
Remainder_A = A - A_eats
# print(A_eats)
# how many B has before she eats any
B = Remainder_A + B
B_eats = B // 2
Remainder_B = B - B_eats

C = Remainder_B + C
C_eats = C // 2
Remainder_C = C - C_eats
A_eats_2 = Remainder_C
A_eats_total = A_eats + A_eats_2

print(A_eats_total)