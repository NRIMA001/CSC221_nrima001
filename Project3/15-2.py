from matplotlib import pyplot as plt
import os

x_values = list(range(5001))
cubes = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Greens, s=10)

ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**3])

plt.show()
script_dir = os.getcwd()
file_path = os.path.join(script_dir, '15-2.png')  
plt.savefig(file_path, dpi=300, bbox_inches='tight')