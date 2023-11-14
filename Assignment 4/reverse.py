numbers = input("Enter a list of numbers: ")
numbers_list = numbers.split()
reverse_numbers = []
for i in range(len(numbers_list)-1, -1, -1):
    reverse_numbers.append(numbers_list[i])

print("The reverse list is: ",reverse_numbers)