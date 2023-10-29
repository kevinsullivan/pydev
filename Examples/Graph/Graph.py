import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Use Pandas to read CSV file into a data frame
# Extract month (x) and profit (y) data into separate series
df = pd.read_csv("data_to_graph.csv")
month = df["month"]
profit = df["profit"]

# Use default Seaborn theme
# Create Seaborn scatter plot with months on x- and profits on y-axis
# Seaborn uses matplotlib, which we call finally to display the plot
# See https://seaborn.pydata.org/generated/seaborn.scatterplot.html
sns.set_theme()
sns.scatterplot(x=month, y=profit)
plt.show()

# To save the graph to a file (e.g., 'output_graph.png'), uncomment and modify the following line:
# plt.savefig('output_graph.png')

# Optional: If you want to save the modified DataFrame back to a CSV file, you can use the following:
# df.to_csv('output_file.csv', index=False)

# Step 4: Close the plot (if you displayed it)
# plt.close()
