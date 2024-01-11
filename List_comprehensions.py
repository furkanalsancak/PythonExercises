
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#----------------------------------------------
#I want n for each n in nums
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)
#------------------------------------------------

#----------------------------------------------
#I want n*n for each n in nums
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# my_list = [n*n for n in nums]
# print(my_list)
#------------------------------------------------

#------------------------------------------------
#using map + lambda
# my_list = map(lambda n: n*n, nums)
# print(my_list)
#------------------------------------------------

#I want n for each n in nums if n is even
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
#print(my_list)

# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

#Using a filter+lambda
# my_list = filter(lambda n: n%2 == 0, nums)
# print(my_list)

# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# list1 = [7,8,9,10,11,12]
# list2 = [1,2,3, 4, 5, 6]

# my_dict = {match1:match2 for match1, match2 in zip(list1,list2) if match1 != 7}
# print(my_dict)

nums2 = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums2:
#     my_set.add(n)
# print(my_set)

# my_set = {n for n in nums2}
# print(my_set)