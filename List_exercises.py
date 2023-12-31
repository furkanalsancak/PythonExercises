'''
my_list = ["The", "Joy", "of", "learning"]
print(len(my_list))

#Adds element to the end of the list
my_list.append("Yes")

#Attaches a list to the current list
my_list.extend(["Furkan", "Hakan", "Levent", "Mehtap"])

#Inserts an element to the indicated index
my_list.insert(2, "Word")

#Removes last element from the list
my_list.pop()

for i in my_list:
    print(i)
'''

#Two ways of creating dictionary
new_dict = dict(
    name = "Kitty",
    age = 1,
    kitten = True
)
# new_dict_2 = {
#     name : "Kitty",
#     age : 1,
#     kitten : True
# }

# value = new_dict.pop("name")
# print(value)

new_dict["is_cool"] = True

for key, value in new_dict.items():
    print(f"{key} : {value}")



names = ["John Python", "Sol Badguy", "Kazuya Mishima", "Terry Bogard"]
name_dict = {}

for i in names:
    names = i.split(" ")
    print(names)

    name = names[0]
    surname = names[1]
    print(surname)
    name_dict[name] = surname

print(name_dict)



mixed_list = [1, 2, "Furkan"]

num_list = []
name_list = []

for i in mixed_list:
    print(type(i))
    i_type = f"{type(i)}"

    if i_type == "<class 'str'>":
        name_list.append(i)
    elif i_type == "<class 'str'>":
        num_list.append(i)



print(num_list)
print(name_list)



###########

nums = [1,2,3,4,5,6,7]

total = 0

for num in nums:
    total += num


print(total)
print(total / len(nums))