import pandas as pd
import numpy as np

new_DS = pd.read_csv(r"C:\Users\MOIZ UDDIN\Downloads\archive\ToyotaCorolla.csv")

DF = pd.DataFrame(new_DS)

# Accessing
km_value_loc = DF.loc[2, 'KM']
# Conditional
Four_Thousand_K_plus_km = DF[DF['KM'] > 100000]

# Exponent = np.exp(DF['KM'])
# For a large dataset:
# Exponent = np.expm1(DF['KM'])

sorted_df = DF.sort_values(by='KM', ascending=False)

# sorted_df.describe()

# To only add number types to perform aggregate functions.
numeric_columns = DF.select_dtypes(include=['number'])
mean_values = pd.DataFrame(numeric_columns.mean())
mean_values

resArr = pd.DataFrame(numeric_columns.groupby('KM').mean())
resArr

del numeric_columns['Age_08_04']

import os

# Change to the directory where the notebook is located
os.chdir(os.path.dirname(os.path.abspath("")))

# Save the CSV file
numeric_columns.to_csv("Book1.csv", index=False)

numeric_columns.to_csv(r"C:\Users\MOIZ UDDIN\Desktop\Python\Book1.csv", index=False)