# Create list to store numbers
numbers = []

# Allow user to fill list using sentinel
while True:
  try:
    num = float(input("Enter a number: "))
  except:
    print("Please enter a number.")
  else:
    # Check for sentinel
    if num < 0:
      break

    # Append to list
    numbers.append(num)

# Create a new list that doubles all of the numbers
new_list = []
for num in numbers:
  new_list.append(num * 2)

for val in new_list:
  print(val, end=" ")