import math

num01 = float(input("Enter the first number: "))

print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.remainder")
print("6.square root")

ask = int(input("Choose an operation among 1 to 6: "))

if ask != 6:
    if ask > 6:
        print("invalid operation")
    else:
        num02 = float(input("Enter the second number: "))
        addition = num01 + num02
        subtraction = num01 - num02
        multiplication = num01 * num02
        division = num01 / num02
        remainder = num01 % num02

square_root = math.sqrt(num01)

if ask == 1:
    print("\nFinal answer is", addition)
elif ask == 2:
    print("\nFinal answer is", subtraction)
elif ask == 3:
    print("\nFinal answer is", multiplication)
elif ask == 4:
    print("\nFinal answer is", division)
elif ask == 5:
    print("\nFinal answer is", remainder)
elif ask == 6:
    print("\nFinal answer is", square_root)
else:
    print("Please choose the correct operation!")

# Hurray!!! Done the project
