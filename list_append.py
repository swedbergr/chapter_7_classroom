# Define list name
sales = []

# Iterate for sales data until sentinel
while True:
  sale = input("Enter the sale or a negative number to end.\n")
  if float(sale) < 0:
    break
  # Append sale to the end of list
  sales += [sale]


# Verify list
print(sales)