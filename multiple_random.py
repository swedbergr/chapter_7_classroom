# Import library
import random

# create list of numbers
numbers = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]

# Get 2 random elements from numbers
selected = random.choices(numbers, k=10)
print(selected)

# Get 2 random elements without duplicates
selected = random.sample(numbers, k=10)
print(selected)