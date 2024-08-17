# Import library and use alias
import matplotlib.pyplot as plt

# Define coordinates
hor = list(range(0, 41, 10))
vert = list(range(100, 501, 100))

# Define titles and axis labels
plt.title("Generic Bar Graph")
plt.xlabel("x-Label")
plt.ylabel("y-Label")

# Change the tick marks for the x-axis

# Customize the bar width (default is 0.8)
bar_width = 6

# Change bar colors
colors = ['r', 'b', 'g', 'c', 'm']

# Create the chart in memory
plt.bar(hor, vert, bar_width, color=colors)

# Display chart from memory
plt.show()