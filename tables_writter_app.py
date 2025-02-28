def print_table(number, up_to=10):
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

# Take user input
try:
    num = int(input("Enter a number: "))
    limit = int(input("*******************Enter the range up to which you want the table*********************: "))
    print_table(num, limit)
except ValueError:
    print("Invalid input. Please enter a valid number.")


def print_table(number, up_to=10):
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

# Take user input
try:
    num = int(input("Enter a number: "))
    limit = int(input("*******************Enter the range up to which you want the table*********************: "))
    print_table(num, limit)
except ValueError:
    print("Invalid input. Please enter a valid number.")

