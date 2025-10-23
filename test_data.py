import pandas as pd

file_data = 'auto-mpg.data'
column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 
                'weight', 'acceleration', 'model year', 'origin', 'car name']

df = pd.read_csv(file_data, delim_whitespace=True, header=None, 
                 names=column_names, na_values='?')
print(f"Data loaded: {len(df)} rows")
print(df.head())