import random

while True:
    user_guess = int(input("Guess a number from 1 to 9 : "))
    random_num = random.randint(1,9)    
    if user_guess < 1 or user_guess > 9:
        print("invalid input. Please try again!!")
        continue
    elif user_guess == random_num:
        print("You guessed correct!!")
        break
    elif user_guess < random_num:
        print("Too low!!")
        continue
    elif user_guess > random_num:
        print("Too high!!")
        continue
    