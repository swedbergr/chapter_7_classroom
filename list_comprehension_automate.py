# Sample list
int_list = [1, 2, 3, 4, 5]
str_list = ["Nebraska", "Kansas", "Wyoming", "Colorado", "South Dakota", "Iowa", "Missouri"]

# Create new list by calculating with every element in the original list
squares = [element**2 for element in int_list]
print(squares)

# Create new list of the length of each string in str_list
str_lengths = [len(state) for state in str_list]
print(str_lengths)

# Create new list that is a subset of other lists based on a condition
even_ints = [element for element in int_list if element % 2 == 0]
print(even_ints)
alph_states = [element for element in str_list if element <= "Nebraska"]
print(alph_states)
