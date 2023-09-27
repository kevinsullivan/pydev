import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a DataFrame
file_path = 'my_file.csv'  
df = pd.read_csv(file_path)

# Step 2: Generate a graph
# Assuming your CSV file has columns 'x' and 'y' for the x and y-axis data
x = df['x']
y = df['y']

# Create a simple line plot
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(x, y, marker='o', linestyle='-')
plt.title('CSV Data Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)

# Step 3: Show the graph or save it to a file
# To display the graph, uncomment the following line:
plt.show()

# To save the graph to a file (e.g., 'output_graph.png'), uncomment and modify the following line:
# plt.savefig('output_graph.png')

# Optional: If you want to save the modified DataFrame back to a CSV file, you can use the following:
# df.to_csv('output_file.csv', index=False)

# Step 4: Close the plot (if you displayed it)
# plt.close()

