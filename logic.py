

grade = 70

#In this if, elif block, the order is wrong.
#Code should have started checking from the highest grade condition,
#and gradually decrease

#Also, instead of greater than(>), the greater than or equal to (>=)
#operator should have been used.
#For example, 70 is Good grade, but here, it can only be seen as pass, 
#rather than good grade
if grade > 40:
    print("Pass!!")
elif grade > 70:
    print("Good!!")
elif grade > 85:
    print("Great!!")
elif grade > 95:
    print("Amazing!!")
elif grade == 100:
    print("You are one of a kind!!!!!!!!!!!")