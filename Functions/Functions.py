import random as rd



def addition(x, y):
    value = x + y
    return value


num_1 = int(input("Please enter a number : "))
num_2 = int(input("Please enter a number : "))

total = addition(num_1, num_2)
print(total)


def get_int(display_string = "Enter number : "):
    '''
    Continues to ask the user for an int until a valid int is entered
    '''
    while True:

        user_input = input(display_string)

        try:
            user_input = int(user_input)
            return user_input
        except:
            print("Please only enter number")


total = 0
while True:
    user_choice = get_int()
    if user_choice == -1:
        break
    total += user_choice

print(f"This is the total : {total}")


#LAMBDA FUNCTIONS

# lambda : print("Hello World")

'''
greeting = lambda : print("Hello World")
greeting()

add_two = lambda x : x + 2
print(add_two(10))
'''

'''
def add_2(x):
    return x + 2
print(add_2(6))

add_two = lambda x : x + 2
print(add_two(5)) 
'''

