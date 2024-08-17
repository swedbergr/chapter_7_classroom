def main():
  # Define list
  names = ["Michael", "Landon", "Eric", "Kristen", "Bailey", "Nancy"]

  # Prompt user for new name
  new_name = input("Provide a name that should be in the list: ")

  # Append name to list if it is not currently in the list
  if new_name not in names:
    names += [new_name]

  # Display names for verification
  print(names)

if __name__ == "__main__":
  main()