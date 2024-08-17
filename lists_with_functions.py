def main():
  print("Press enter to fill a list of integers.")
  input()
  # Get list of integers
  numbers = fill_list()

  # Get average of list
  print("Press enter to calculate the average of the numbers.")
  input()
  average = get_average(numbers)
  print(average)


def fill_list():
  '''
  This function gets numbers from user and puts them in a list and returns the list.
  return: list if integers.
  '''
  # Create list to store numbers
  numbers = []

  # Allow user to fill list using sentinel
  while True:
    try:
      num = int(input("Enter an integer: "))
    except:
      print("Please inter an integer.")
    else:
      # Check for sentinel
      if num < 0:
        break

      # Append to list
      numbers.append(num)

      # Return list
      return numbers

def get_average(test_list):
  '''
  This function gets a list argument, calculates the average and returns the average.
  param test_list: list of integers
  return: float value for average in list
  '''
  average = sum(test_list) / len(test_list)
  return average


if __name__ == "__main__":
  main()