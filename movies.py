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
# DO SOMETHING INTERESTING HERE TO THE DATA
#

# Output the updated data to output.xlsx Excel file
df.to_excel("output.xlsx")
print("\nVerify expected output file")
df = pd.read_excel("output.xlsx")
print(df.describe)
