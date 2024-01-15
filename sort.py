import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# li = [9,1,8,2,7,3,6,4,5]

# s_li = sorted(li, reverse=True)
# print("Sorted variable:\t", s_li)

# li.sort(reverse=True)

# print("Original variable:\t", li)

tup = (9,1,8,2,7,3,6,4,5)

print("Tuple\t", )

li = [-6,-5,-4,1,2,3]
s_li = sorted(li, key=abs)
print(s_li)