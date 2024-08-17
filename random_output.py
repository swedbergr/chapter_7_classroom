# Import library
import random

# Identify list name
names = []

# Get elements for list from user
while True:
  new_name = input("Enter a name just hit enter to gerenate random name : ")
  # Sentinel
  if new_name == "":
    break

  # Append name to list
  names.append(new_name)


# Generate random index
random_index = random.randrange(len(names))

# Print random name from list
print(names[random_index])