"""
This program reads an Excel spreadsheet,
specified by a file path embedded in the
code, into a pandas dataframe. The data can
be processed. Finally, this program writes
the possibly updated dataframe to the Excel
file called output.xsls. No libraries beyond
pandas are needded for this simple task. 
"""

import pandas as pd

# read data from movies Excel file
df = pd.read_excel("movies.xls")

print("Summarize input data: ", df.describe)

#
# Add here what you want to do with the data
#

# Output the updated data to output.xlsx Excel file
df.to_excel("output.xlsx")


print("\nRead it back in and summarize it")
df = pd.read_excel("output.xlsx")
print(df.describe)
