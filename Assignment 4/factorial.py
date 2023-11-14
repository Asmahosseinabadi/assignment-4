number = int(input("enter a number: "))
i = 1
factorial = 1
while factorial < number:
    i += 1
    factorial *= i
if factorial == number:
    print("YES")
else:
    print("NO")