
# test_bool = True
# test_float = 0.12345
# test_int = 9

# display_string = "This is the Bool value: {}\nThis is the Float value: {}\nThis is the Int value: {}".format(test_bool, test_float, test_int)
# print(display_string)



# value = 10

# for x in range(0, value, 2):
    
#     print(x)


# word = "coffee"
# final_word = ""
# word_length = len(word)

# for i in range(word_length):
#     if i % 2 == 0:
#         final_word += word[i].upper()
#     else:
#         final_word += word[i].lower()

# print(final_word)
# print(word_length)

# num_list = [1, 2, 3, 4, 5]
# found = False
# num = int(input("Input a number from 1 to 10 and find out if it's in our list:"))
# if num<1 or num>10:
#     print("Number out of range")
# else:
#     for number in num_list:
#         if num == number:
#             found = True
#             break
#     print(f'List contains {num}: {found}')

# print("Hello World")

# name = "Jimmy"
# age = 23
# print("Hello " + name + ", you are " + str(age) + " years old")


# age = "32"

# months_age = age * 12

# sentence = "Hello World" # space counts as index
# final_string = ""

# for i in range(len(sentence)):
#     if i % 2 == 1: # odd
#         final_string += sentence[i].upper()
#     else:
#         final_string += sentence[i].lower()
    
# print(final_string)


# number_builder = ""
# i = 0
# while i <= 50:
#     if i % 2 == 0:
#         number_builder += str(i) + " "
#     i += 1
# print(number_builder)

# number_builder = [] #note the variable has to be a list rather than a string
# i = 0
# while i <= 50:
#     if i % 2 == 0:
#         number_builder.append(str(i))
#     i += 1
# print(" ".join(number_builder))


# my_dictionary = {
#     "name" : "Furkan",
#     "age" : 22,
#      "is_funny" : True
# }

# for i, j in my_dictionary.items():
#     print(i, j)

# print(my_dictionary)
# print(my_dictionary["age"])

# cat = dict(name = "kitty", age = 0.5)
# print(cat)

# cat["colour"] = "white"
# print(cat)

# popped_pair = cat.pop("colour")
# print(cat)
# print(popped_pair)
    
'''
num_list = ['1', '5', '8', '14', '25', '31']
new_num_list_ints = [int(element) for element in num_list]
by_two_num_list = [int(element)*2 for element in num_list]
print(num_list)
print(new_num_list_ints)
print(by_two_num_list)
'''


# prompt_text = '''
#     Enter
#     text here
# '''
# name = input(prompt_text)
# print(name)

# string = "my name is furkan"
# list_string = string.split(" ")
# print(list_string)
# capitalize_list_string = []
# for i in range(len(list_string)):
    
#     capitalize_list_string+= [list_string[i].capitalize()]

# # for i in list_string:
    
# #     capitalize_list_string += [i[0].upper() + i[1:]]
#     # print(i[0].upper() + i[1:])

# print(capitalize_list_string)

# string = "my name is furkan"
# capitalized_string = string.title()
# print(capitalized_string)


# string = "my name is furkan"
# list_string = string.split()

# capitalize_list_string = []
# for word in list_string:
#     capitalize_list_string.append(word.capitalize())

# result_string = ' '.join(capitalize_list_string)
# print(result_string)

'''
word = "supercalifragilisticexpialidocious"
word2 = []

for i in range(len(word)):
    if i % 2 == 0:
        word2.append(word[i].upper())
    elif i % 2 == 1:
        word2.append(word[i].lower())

print("".join(word2))
'''


# number = input("Enter a number : ")



# if number == number[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# try:
#     number = int(input("Enter a number: "))
#     # Check for palindrome
#     if str(number) == str(number)[::-1]:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")   



# def insert_obj(list_to_edit, obj_to_add, index_of_item):

#     current_list = list_to_edit
#     current_index = index_of_item
#     try:
#         current_index = int(current_index)
#     except:
#         print("Please enter int as an index value")
        
#     current_list.insert(index_of_item,obj_to_add)
#     return current_list

# same_list = ['A','B','C','D','E']
# same_list = insert_obj(same_list, "D", 3)
# print(same_list)

'''
test_string = "This is * a test"

split_string = test_string.split("*")
joined_list = "*".join(split_string)
# another_test = " ".join(test_string)

print(split_string)

count = 0
for char in joined_list:
    if char.upper() == "T":
        count += 1

print(f"This is the number of this char : {count} ")

joined_list = joined_list.replace("i", "I", 5)
print(joined_list)
'''

'''
numbers = [1,2,3,4,5]

for num in range(len(numbers)):
    print(numbers[num])
    numbers[num] = str(numbers[num])

print(numbers)
'''


'''
test_dict = {
    "name" : "Chris"
}

test_dict["is_funny"] = False

print(test_dict)
print(test_dict["name"])
'''

user_db = []
user = {"username" : "", "password": ""}

while True:
    user_input = input("Would you like to log in or register? (Enter: login/register)")

    if user_input.strip() == "register":
        user["username"] = input("Please enter your desired name: ")
        user["password"] = input("Please enter your desired password: ")
        
        is_unique = True
        for account in user_db:
            if account["username"] == user["username"]:
                is_unique = False

        if is_unique:
            user_db.append(user)
            print("User registered")
        else:
            print("Cannot register user, username taken")
    if user_input == "-1":
        break