my_list = []

#adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting a new value at index 1
my_list[1] = 15
print(my_list)

#a second list
list2 = [50, 60, 70]

#extending my_list with list2
my_list.extend(list2)
print(my_list)

#removing the last element from my my_list
my_list.pop()
print(my_list)

#sorting the list
my_list.sort()

#finding the index of the value 30. If the value is in the list, print the index
if 30 in my_list:
    index_30 = my_list.index(30)
    print("Index of 30 in my list: ", index_30)

else: 
    print("30 is not in the list")
