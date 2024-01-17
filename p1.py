import pandas as pd

csv_file_path = 'Data/1.csv'
df = pd.read_csv(csv_file_path)
print("Numeric Data:")
print(df)


column_sums = df.sum()
print("\nColumn Sums:")
print(column_sums)


column_means = df[['Age','Salary','Tax']].mean()
print("\nColumn Means:")
print(column_means)


column_max = df[['Age','Salary','Tax']].max()
print("\nColumn Max Values:")
print(column_max)
