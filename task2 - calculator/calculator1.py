
print("----- Basic Calculator -----")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Power (**)")

ch = int(input("\nEnter your choice (1,2,3,4,5): "))
match ch:
    case 1:
        print(f"\nResult: {num1} + {num2} = {num1 + num2}")
    case 2:
        print(f"\nResult: {num1} - {num2} = {num1 - num2}")
    case 3:
        print(f"\nResult: {num1} * {num2} = {num1 * num2}")
    case 4:
        if num2 != 0:
            print(f"\nResult: {num1} / {num2} = {num1 / num2}")
        else:
            print("\nError You cannot divide by zero.")
    case 5:
        print(f"\nResult: {num1} ** {num2} = {num1 ** num2}")
    case _:  
        print("Unknown choice")
