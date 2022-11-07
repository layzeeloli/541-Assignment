print("Select an operation to perform: ")
print("A. ADD")
print("B. SUBTRACT")
print("C. MULTIPLY")
print("D. DIVIDE")

operation = input()

if operation == "A":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The answer is " + str(int(num1) + int(num2)))
elif operation == "B":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The answer is " + str(int(num1) - int(num2)))
elif operation == "C":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The answer is " + str(int(num1) * int(num2)))
elif operation == "D":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The answer is " + str(int(num1) / int(num2)))
else:
    print("Invalid input.")