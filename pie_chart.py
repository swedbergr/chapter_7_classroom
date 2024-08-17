# Import library with alias
import matplotlib.pyplot as plt

# Create list of values for pie chart
values = [20, 60, 80, 40]

# Create list of labels for each value
slice_labels = ["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"]

# Add a title
plt.title("Random Pie Chart")

# Change slice colors
slice_colors = ['r', 'b', 'g', 'c']

# Create the chart in memory
plt.pie(values, colors=slice_colors, labels=slice_labels)

# Display chart from memory
plt.show()