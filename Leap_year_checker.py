def is_leap_year(year):
    # A leap year is divisible by 4
    # But if it’s divisible by 100, it must also be divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Take user input
try:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Invalid input. Please enter a valid year.")

