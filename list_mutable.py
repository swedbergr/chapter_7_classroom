# Set constant for the number of days
DAYS = 5

# Create list to hold the correct number of elements
sales = [0] * DAYS

# Iterate to fill list
for index in range(len(sales)):
  sales[index] = input(f"Enter the sales for day {index + 1}: ")

# Print list to verify
print(sales)