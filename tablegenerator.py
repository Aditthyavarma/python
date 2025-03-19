print("Multiplication Table Generator")

# Taking user input
num = int(input("Enter the number for the table: "))
range_upto = int(input("Enter the range up to which table is needed: "))

print(f"Multiplication Table for {num} up to {range_upto}:")
for i in range(1, range_upto + 1):
    print(f"{num} x {i} = {num * i}")
