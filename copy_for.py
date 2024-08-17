list1 = [1, 2, 3, 4, 5]
list2 = []
for item in list1:
  list2.append(item)

print(list1)
print(list2)

list2[0] = 10

print(list1)
print(list2)