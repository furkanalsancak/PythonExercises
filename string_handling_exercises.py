
some_string = "Hello World"
final_string = ""

some_string_2 = "I am learning to code"
final_string_2 = []

for i in range(len(some_string)):
    if i % 2 == 0:
        final_string += some_string[i].upper()
    else:
        final_string += some_string[i].lower()
print(final_string)

some_string_2_split = some_string_2.split(" ")
for i in range(len(some_string_2_split)):
    if i % 2 == 0:
        final_string_2.append(some_string_2_split[i].upper())
    else:
        final_string_2.append(some_string_2_split[i].lower())

final_string_2_joined = " ".join( final_string_2)
print(final_string_2_joined)