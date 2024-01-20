
# creating total variable to calculate the sum of inputted numbers
total = 0
#creating count variable to calculate the number of inputs
count = 0
#creating average variable to calculate the average of numbers entered
avg = 0

#asking user to enter number
user_input = int(input("Enter a number (-1 to exit) : "))

#This while loop will run as long as entered number is not -1
#the while loop increments total value by the entered number, and increments count by 1
#then the loop asks the user to enter another integer. This process keeps going until user enters -1
#when user enters -1, average is calculated, and loop exits
while user_input != -1:
    total += user_input
    count += 1
    user_input = int(input("Enter a number (-1 to exit) : "))
    if user_input == -1:
        avg = total / count
        print("Total : " + str(total))
        print("Average : " + str(avg))
        print("Program exitted!!")
        break