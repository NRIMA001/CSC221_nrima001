import matplotlib.pyplot as plt
import seaborn as sns
import os

x_values = list(range(5001))
cubes = [x**3 for x in x_values]
fig, ax = plt.subplots(figsize=(10, 6))  # Set figure size for better readability

# Set plot style using seaborn's API
sns.set_style('whitegrid')

#scatter plot
ax.scatter(x_values, cubes, s=10, label='Cubes')  # Add label for legend

# Set chart title and label axes
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Set axis limits
ax.set_xlim(0, x_values[-1] * 1.05)  # Add 5% margin to x-axis
ax.set_ylim(0, max(cubes) * 1.05)  # Add 5% margin to y-axis

#Adding legend
ax.legend(loc='upper right')

#Tried to save the png file to the same directory
script_dir = os.getcwd()  # Get the current working directory
file_path = os.path.join(script_dir, '15-1.png')  # Construct the file path
plt.savefig(file_path, dpi=300, bbox_inches='tight')  # Set dpi and bounding box for better image quality

# Show plot
plt.show()
