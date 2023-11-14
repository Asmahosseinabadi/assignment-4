list = input("Enter a list1 of numbers: ")
numbers_list = list.split()
new_list = []
for element in list:
    if element not in new_list:
        new_list.append(element)
print("the new list is: ",new_list)