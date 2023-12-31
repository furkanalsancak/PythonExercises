

#if statement, elif statement, else statement
#boolean
#operators

'''

    if <condition>
        <statement>

'''

IsRain = True

if IsRain == False:
    print("The sky is clear!!")

else:
    print("It is raining!!")

grade = int(input("Enter your exam mark : "))

'''
== is equal to
>= greater than / equal to
<= less than / equal to
!= not equal to
'''
if grade >= 70:
    print("You have scored above the average mark!!")
elif grade >= 50:
    print("You passed with an average mark!!")
elif 40 <= grade < 50: # grade < 50 and grade > 30
    print("You scored below the average grade!!")
else:
    print("You have failed the class!!")
