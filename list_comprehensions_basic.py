# Sample list
list1 = [1, 2, 3, 4, 5]

# Sample way to copy list
list2 = []
for element in list1:
  list2.append(element)

print(list2)

# Copy list with list comprehension
list3 = [element for element in list1]

print(list3)