# empty list
from typing import List


empty_lists = []

# lists with same elements

list1 = [1, 2,7,4,20,50]

# lists with different elements

list2 = [2, "otto", "##", 2.5]

print(list1, list2, empty_lists)

# output
# [1, 2, 7, 4, 20, 50] [2, 'otto', '##', 2.5] []

print(len(list2))   #to know the number of items in a given set

for i in range (len(list2)):
    print(list2[i])

# to determin the max and min element in the list
list3 = [342.73,
818.99,
891.13,
623.9,
688.64,
801.57,
447.33,
175.67,
209.21,
979.91]

print (len(list3))

print(max(list3))

print(min(list3))

list3.sort()
print(list3)

list3.sort(reverse=True)

print(list3)



