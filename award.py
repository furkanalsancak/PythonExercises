swimming_time = float(input("Enter swimming time (minutes): "))
cycling_time = float(input("Enter cycling time (minutes): "))
running_time = float(input("Enter running time (minutes): "))

total_time = swimming_time + cycling_time + running_time

if 0 <= total_time <= 100:
    award = "Provincial Colours"
elif 101 <= total_time <= 105:
    award = "Provincial Half Colours"
elif 106 <= total_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"

print("Total time:", total_time, "minutes")
print("Award:", award)