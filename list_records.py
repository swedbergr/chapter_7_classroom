# List for student records
students = ["Luke", "Johnson", 12, "Ashtian", "Nielsen", 12, "Mason", "Taylor", 12]

# Use for loop with range to create a list of indexes for students
for index in range(0, len(students), 3):
  print(f"{students[index]} {students[index + 1]}: {students[index + 2]}")