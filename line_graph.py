# Import library with alias
import matplotlib.pyplot as graph

# Define coordinate lists
x_coords = [0, 1, 2, 3, 4]
y_coords = [0, 3, 1, 5, 2]

# Add title
graph.title("Students Requesting Help")

# Add axis labels
graph.xlabel("Day of the week")
graph.ylabel("Number of students")

# Show grid
graph.grid(True)

# Change the displayed domain (x-axis values) and range (y-axis values)

# Change tick marks for each axis
graph.xticks(x_coords, ["Mon", "Tues", "Wed", "Thu", "Fri"])
graph.yticks(range(6), ["0 Students", "1 Student", "2 Students", "3 Students", "4 Students", "5 Students"])

# Create a plot and store in memory
graph.plot(x_coords, y_coords)


# Display plot stored in memory
graph.show()