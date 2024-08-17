# Sample tuple
tup = (1, 2, 3, 4, 5)

# Cast to a temporary list
temp = list(tup)

# Append to the list
temp.append(6)

# Cast list to tuple and reassign tup variable
tup = tuple(temp)

# Print tup for display
print(tup)