# DATA WRANGLING WITH PANDAS

import pandas as pd

# Reading in csv files:
csv_data = pd.read_csv('training-set.csv')

# Pandas loads the csv data into a DataFrame (table)
# Displaying the DataFrame:
csv_data.head()

# In Pandas, columns are called 'series'
# The describe function shows a table of statistics about the data in your DataFrame
csv_data.describe(include='all')

# Shuffling your DataFrame
csv_data = csv_data.sample(frac=1).reset_index(drop=True)


# You can print out all columns (series) in the DataFrame using:
csv_data.columns
# Then print out contents of one of the listed columns by passing in its name
csv_data['employee_name']

## Viewing multiple columns from DataFrame
# By passing in array of column names to index:
csv_data[['employee_name','email']]

# Or by indexing a range of columns:
cols_2_4 = csv_data.columns[2:4]
csv_data[cols_2_4]

# Accessing rows by index:
csv_data.iloc[5]

# Accessing multiple rows
csv_data.iloc[5:10]

# EXAMPLES
# Accessing row 5 of column named 'employee_salary'
csv_data['employee_salary'].iloc[4]

# Accessing subset of rows and subset of columns:
cols_2_4 = csvdata.columns[2:4] # First choose the column names
cols_2_4 = csv_data[cols_2_4] # Then we get the columns
cols_2_4.iloc[5:10] # Now select the rows from that DataFrame (subset)

csv_data[csv_data.columns[2:4]].iloc[5:10] # Same expression in one line
