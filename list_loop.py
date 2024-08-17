new_list = [1, 2, 3, 4]

# For loop to access each element
for num in new_list:
  print(num)


# For loop to demonstrate how the loop's variable does not change the list elements
for num in new_list:
  num = 10

print(new_list)