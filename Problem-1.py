#Input values
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))
#Mathematical Operations
print("Operations to Perform\n")
print("Enter 1 for Addition")
print("Enter 2 for Subtraction ")
print("Enter 3 for Multiplication")
print("Enter 4 for Division\n")
operation = int(input("Enter Action to perform : "))
if operation == 1:
    print("Addition of GIven Two Numbers is : " + str((num1 + num2)))
elif operation == 2:
    print("Subtraction of GIven Two Numbers is : " + str(-(num1 - num2)))
elif operation == 3:
    print("Multiplication of GIven Two Numbers is : " + str((num1 * num2)))
elif operation == 4:
    print("Division of GIven Two Numbers is : " + str((num1 / num2)))
else:
    print("You have Entered invalid number")
