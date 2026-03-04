import numpy as np

print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
print("6. Power operation")
print("7. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        h = int(input("Enter how many numbers you want to add: "))
        l1 = []
        for i in range(h):
            num = int(input(f"Enter number {i+1}: "))
            l1.append(num)
        arr = np.array(l1)
        ans = np.sum(arr)
        print("Addition answer is:", ans)

    elif choice == 2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        ans = a - b
        print("Subtraction answer is:", ans)

    elif choice == 3:
        ans = 1
        print("Enter numbers to multiply (enter 0 to stop):")
        while True:
            a = int(input("Enter number: "))
            if a == 0:
                break
            ans = ans * a
        print("Multiplication answer is:", ans)

    elif choice == 4:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        while b == 0:
            print("Division by zero Error. Enter a valid number.")
            b = int(input("Enter denominator: "))
        ans = a / b
        print("Division answer is:", ans)

    elif choice == 5:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        while b == 0:
            b = int(input("Division by zero. Enter valid number: "))
        ans = a % b
        print("Modulo answer is:", ans)

    elif choice == 6:
        a = int(input("Enter base value: "))
        b = int(input("Enter power value: "))
        ans = a ** b  # In Python, ** is used for power, ^ is for XOR
        print("Power result:", ans)

    elif choice == 7:
        print("Exiting....")
        break

    else:
        print("Invalid choice")
