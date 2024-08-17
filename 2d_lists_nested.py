def main():
  # Create list to hold students
  students = []
  # Create menu to run the program
  while True:
    print("What would you like to do?")
    print("1. Add Records",
          "\n2. View Records",
          "\n3. Quit")
    choice = input()
    if choice == "1":
      students += add_records()
    elif choice == "2":
      view_records(students)
    elif choice == "3":
      break
    else:
      print("That is not a valid option. Please try again.")


def add_records():
  '''
  This function allows the user to add records to a list, and then returns the list.
  return: list of records where each element is a list containing two string elements and an int element
  '''
  # Create sentinel and list to hold records
  another_record = "y"
  students = []

  # Iterate for each record
  while another_record == "y" or another_record == "Y":
    first = input("First name: ")
    last = input("Last name: ")
    # Validate grade is an int
    while True:
      try:
        grade = int(input("Grade: "))
      except ValueError:
        print("Please enter a number for grade.")
      else:
        break

    # Append record as a list to the list
    students.append([first, last, grade])

    # Check for more records
    another_record = input("Whould you like to enter another record? (y or n)")

  # Return list
  return students


def view_records(students):
  '''
  This function takes a two-dimensional list of student records and displays them.
  param students: two-dimensional list where the outer list is a record and the inner list
  contains a first name (str), last name (str) and grade (int).
  '''
  # Iterate for each record
  for record in students:
    # Iterate for each field
    for field in record:
      print(field)



# Run main function
if __name__ == "__main__":
  main()