import pandas as pd

df = pd.read_csv('earthquakeData.csv')

# List of columns to be dropped
columns_to_drop = ['nst', 'gap', 'dmin', 'horizontalError', 'magError', 'magSource']

# Drop the specified columns
df.drop(columns=columns_to_drop, inplace=True)

# Save the edited DataFrame back to the original CSV file
df.to_csv('earthquakeData.csv', index=False, header=false)
