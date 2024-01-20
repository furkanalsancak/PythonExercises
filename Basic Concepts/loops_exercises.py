

#Exercise 1: Print First 10 natural numbers using while loop
'''
print("Exercise 1")
i=1
while i <= 10:
    print(i)
    i += 1
'''


#Exercise 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
#print()
'''
print("Exercise 2")
row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")
'''
    

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
#print()
'''
print("Exercise 3 ")
user_input = int(input("Please enter a number : "))
sum = 0
for i in range(0, user_input+1):
    sum = sum + i

print("Total sum " + str(sum))
'''
#or
'''
user_input = int(input("Please enter a number : "))
sum = sum(range(1, user_input + 1))
print("Total sum " + str(sum))
'''

# Exercise 4: Write a program to print multiplication table of a given number
'''
print()
print("Exercise 4 ")
num = 5
for i in range(1, 11):
        print(num * i)
'''

#Exercise 5: Display numbers from a list using loop
'''
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
'''
    
    
#Exercise 6: Count the total number of digits in a number
'''
number = 75869
number_str = str(number)
counter = 0
for digit in number_str:
    counter += 1

print(counter)
'''
#another solution
'''
num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10

    # increment counter by 1
    count = count + 1
print("Total digits are:", count)
'''

#Exercise 7: Print the following pattern
'''
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
'''

# Exercise 8: Print list in reverse order using a loop
'''
list1 = [10, 20, 30, 40, 50]
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])

#another solution
list1 = [10, 20, 30, 40, 50]
reversed_list = reversed(list1)
for i in reversed_list:
    print(i)
'''

# Exercise 9: Display numbers from -10 to -1 using for loop
'''
for i in range(-10, 0, 1):
    print(i)
'''


# Exercise 10: Use else block to display a message “Done” 
# after successful execution of for loop
'''
for i in range(6):
    if i < 5 :
        print(i)
    else:
        print("Done!")
'''
'''
for i in range(5):
    print(i)
else:

    print("Done!")
'''

# Exercise 11: Write a program to display all prime numbers within a range
'''
start = 25
end = 50

for i in range(start, end, 1):
    if i % 2 == 1:
        print(i)
'''

'''
string = "coffee"
for char in range(-1, -(len(string))-1, -1):
    print(string[char])
'''

'''
list = []
while True:
    user_input = input("Enter : ")
    
    list.append(user_input)
    yesOrNo = input("Do you want to continue? (y or n): ")
    if yesOrNo == "y":
        continue
    else:
        break
print(list)
'''

'''
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    
    return leap

year = int(input("Enter a year: "))
print(is_leap(year))
'''

'''
list = [1,3,2,34,10,23]
list.sort()
print(list[-2])
'''


#*
#**
#***
#****
#*****
#****
#***
#**
#*
#loop for nine rows of our pattern
#increase number of stars in pattern until the 5th row is reached
#Then decrease the pattern

pattern = "*"
for row in range(10):
    
    if row <= 5:
        print(pattern * row)
    else:
        print(pattern * (10 - row))