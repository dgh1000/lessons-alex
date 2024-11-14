first_name = input()
last_name = input()

first_name = first_name.lower()
last_name = last_name.lower()
part1 = first_name[0]
part2 = last_name[0] + last_name[len(last_name)-1]
part3 = str(len(first_name))

username = part1 + part2 + part3

letter_count = [0] * 26
for letter in username:
    if letter.isalpha():
        index = ord(letter) - ord("a")
        letter_count[index] += 1
for count in letter_count:
    if count > 1:
        username += "x"
        break

print(username)

# we left off here