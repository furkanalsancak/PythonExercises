pattern = "@"
for i in range(1, 14):
    to_print = pattern*i
    if i >=7:
        count_down = 14 - i
        to_print = pattern*count_down
    
    print(to_print)