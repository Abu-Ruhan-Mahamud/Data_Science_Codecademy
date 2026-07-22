import codecademylib3_seaborn
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

data = [[0,0], [1,0], [0,1], [1,1]]
labels = [0, 0, 0, 1]
# Plot Data
plt.scatter([point[0] for point in data], 
            [point[1] for point in data], 
            c=labels,
            cmap='coolwarm')

plt.show()



# Create a Perceptron object named classifier
classifier = Perceptron(max_iter=40, random_state=22)

# Train the model
classifier.fit(data, labels)

# Validate the model
print("Accurarcy: ", classifier.score(data, labels))



# Create Data
data = [[0,0], [1,0], [0,1], [1,1]]
labels = [0, 1, 1, 0]
# Plot Data
plt.scatter([point[0] for point in data], 
            [point[1] for point in data], 
            c=labels,
            cmap='coolwarm')


plt.show()

# Create a Perceptron object named classifier
classifier = Perceptron(max_iter=40, random_state=22)

# Train the model
classifier.fit(data, labels)

# Validate the model
print("Accurarcy: ", classifier.score(data, labels))


# Create Data
data = [[0,0], [1,0], [0,1], [1,1]]
labels = [0, 1, 1, 1]
# Plot Data
plt.scatter([point[0] for point in data], 
            [point[1] for point in data], 
            c=labels,
            cmap='coolwarm')

# Create a Perceptron object named classifier
classifier = Perceptron(max_iter=40, random_state=22)

# Train the model
classifier.fit(data, labels)

# Validate the model
print("Accurarcy: ", classifier.score(data, labels))


# Reset labels to be representing an AND gate
data = [[0,0], [1,0], [0,1], [1,1]]
labels = [0, 0, 0, 1]
# Return distance of points from the decision boundary
classifier.decision_function([[0, 0], [1, 1], [.5, .5]])




# Create a list of the points we want to input to .decision_function()
x_values = np.linspace(0, 1, 100) # list of 100 evenly spaced decimals between 0 and 1
y_values = np.linspace(0, 1, 100) 

# Find every possible combination of those x and y values
point_grid = list(product(x_values, y_values))

# Store the distances from the boundary for each point
distances = classifier.decision_function(point_grid)

# abs() returns the absolute value of a number
abs_distances = [abs(pt) for pt in distances]

# Turn the distances into a NumPy array
distances_matrix = np.reshape(abs_distances, (100, 100))

# Plot the distance data in heatmap
heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)
plt.colorbar(heatmap) # Put legend on heatmap
plt.scatter([point[0] for point in data], 
            [point[1] for point in data], 
            c=labels) # Add points to plot
plt.show()


# Create a list of the points we want to input to .decision_function()
x_values = np.linspace(0, 1, 100)  # List of 100 evenly spaced decimals between 0 and 1
y_values = np.linspace(0, 1, 100)

# Find every possible combination of those x and y values
point_grid = list(product(x_values, y_values))

# Store the distances from the boundary for each point
distances = classifier.decision_function(point_grid)

# Abs() returns the absolute value of a number
abs_distances = [abs(pt) for pt in distances]

# Turn the distances into a NumPy array
distances_matrix = np.reshape(abs_distances, (100, 100))

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the heatmap with contour lines
heatmap = ax.contourf(x_values, y_values, distances_matrix, cmap='viridis', levels=np.linspace(np.min(distances_matrix), np.max(distances_matrix), 20))


# Add contour lines to indicate decision boundaries
contours = ax.contour(x_values, y_values, distances_matrix, levels=[0], colors='red', linestyles='dashed')
ax.clabel(contours, inline=True, fontsize=10, fmt=lambda val: 'Decision Boundary')


# Add a colorbar for reference
cbar = plt.colorbar(heatmap, ax=ax)
cbar.set_label('Distance from Boundary')

# Scatter plot of data points with colors representing labels
scatter = ax.scatter([point[0] for point in data], 
                     [point[1] for point in data], 
                     c=labels, cmap='coolwarm', edgecolors='k', s=50)
plt.colorbar(scatter, ax=ax, label='Labels')

# Set axis labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Decision Function Heatmap with Decision Boundary')

plt.show()







