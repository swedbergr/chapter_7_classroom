def main():
  # Create a menu to demonstrate lists with files
  while True:
    print("What would you like to do?")
    print("1. Write list elements to a file",
         "\n2. Read items in a file into a list",
         "\n3. Sort items in a file", 
         "\n4. Quit")
    choice = input()

    # Navigate user based on choice
    if choice == "1":
      write_file()
    elif choice == "2":
      read_file()
    elif choice == "3":
      sort_file()
    elif choice == "4":
      break
    else:
      print("That is not a valid input. Please try again.")


def write_file():
  '''
  This function collects elements from a user, stores them in a list and writes them to a file.
  '''
  # Create list
  new_list = []
  # Get elements for list
  while True:
    element = input("Enter element to list or press enter to finish: ")
    # Sentinel
    if element == "":
      break

    # Append element to list with \n for file
    new_list.append(element + "\n")

  # Write whole list to file
  with open("sample.txt", "w") as outfile:
    outfile.writelines(new_list)



def read_file():
  '''
  This funciton reads the elements from a file into a list and displays the list.
  '''
  # Convert file into list
  with open("sample.txt", "r") as infile:
    new_list = infile.readlines()

  # Iterate through list
  for element in new_list:
    # Dispay element without \n character
    print(element.rstrip("\n"))


def sort_file():
  '''
  This function sorts the elements of a file.
  '''
  # Fill list from file
  with open("sample.txt", "r") as infile:
    new_list = infile.readlines()
    
  # Sort list
  new_list.sort()

  # Re-write file from sorted list
  with open("sample.txt", "w") as outfile:
    outfile.writelines(new_list)



# Execute main
if __name__ == "__main__":
  main()