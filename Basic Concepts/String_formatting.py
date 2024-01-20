
# for i in range(1,11):
#     sentence = "The value is {:03}".format(i)
#     print(sentence)

# pi= 3.14159265

# sentence = "Pi is equal to {:.2f}".format(pi)
# print(sentence)

# sentence = "1 MB is equal to {:,.2f}".format(1000**2)
# print(sentence)


import datetime
my_date = datetime.datetime(2016,9,24,12,30,45)

# sentence = "{:%B %d, %Y}".format(my_date)
# print(sentence)

sentence = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(my_date)
print(sentence)