import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a Pandas DataFrame
file_path = 'data.csv'  
df = pd.read_csv(file_path)

# Step 2: Extract month (x) and profit (y) data into series
month = df['month']
profit = df['profit']

# Use default Seaborn theme
# Create a scatter plot using Seaborn
# See https://seaborn.pydata.org/generated/seaborn.scatterplot.html
sns.set_theme()
sns.scatterplot(x=month, y=profit)

# Seaborn uses matplotlib, which we call to display the plot
plt.show()


# To save the graph to a file (e.g., 'output_graph.png'), uncomment and modify the following line:
# plt.savefig('output_graph.png')

# Optional: If you want to save the modified DataFrame back to a CSV file, you can use the following:
# df.to_csv('output_file.csv', index=False)

# Step 4: Close the plot (if you displayed it)
# plt.close()

