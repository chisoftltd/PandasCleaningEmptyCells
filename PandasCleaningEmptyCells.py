# Pandas - Cleaning Empty Cells
# Empty Cells
# Remove Rows
import pandas as pd 
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())
print()

# If you want to change the original DataFrame, use the inplace = True argument
df.dropna(inplace = True)
print(df.to_string())
print()

# Replace Empty Values
df = pd.read_csv('data1.csv')

df.fillna(1.39, inplace = True)
print(df.to_string())

# Replace Only For a Specified Columns
df = pd.read_csv('data2.csv')

df["Credit Amount"].fillna(12.39, inplace = True)
print(df.to_string())
print()

# Replace Using Mean, Median, or Mode
# Using MEAN
df = pd.read_csv('data3.csv')
x = df["Debit Amount"].mean()
df["Credit Amount"].fillna(x, inplace = True)
print(df.to_string())
print()

# Using MEDIAN
df = pd.read_csv('data3.csv')
x = df["Debit Amount"].median()
df["Credit Amount"].fillna(x, inplace = True)
print(df.to_string())
print()


# Using AVERAGE
df = pd.read_csv('data3.csv')
x = df["Debit Amount"].mode()[0]
df["Credit Amount"].fillna(x, inplace = True)
print(df.to_string())
print()