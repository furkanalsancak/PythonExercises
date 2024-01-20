
# # Printing the star pattern using a single for loop
# for i in range(1, 10):
#     if i <= 5:
#         print('*' * i)
#     else:
#         print('*' * (10 - i))

# print()

# # Printing the star pattern using two for loops
# for i in range(1, 6):
#     print("*" * i)

# #iterate backwards, rather than forwards, using -1
# for i in range(4, 0, -1):
#     print("*" * i)

'''
user_input = int(input("Enter the number of stars : "))
for i in range(0, user_input):
    stars = "*"
    print(i * stars)

for i in range(user_input, 0, -1):
    stars = "*"
    print(i * stars)

'''

pattern = ""

count_up = 4
hole = ""

for num in range(9):

    if num <= 4:
        spaces = " " * (count_up - num)

        if num < 3:
            pattern += "*"
        else:
            hole += "  "



    else:
        spaces = " " * (num - count_up)

        if num == 5:
            hole = "  "
        else:
            hole = ""

        if num >= 7:
           pattern = "*" * (9 - num)

    print(f"{spaces}{pattern}{hole}{pattern}")