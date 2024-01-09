import pandas as pd
import numpy as np

areey = np.array([[1, 2, 3], [4, 5, 6]])
flattened_array = areey.flatten()

index=[1,2,3,4,5,6]

arr = pd.Series(data=flattened_array,index=index)
# print(arr)

# Accessing vals same as previous ones:
# print(arr[1])
# print(arr[[1,3,4]])

# Conditionals:
# Get data:
# print(arr[arr>2])
# get index:
# print(arr[arr>2].index)

# Take exponent:
# print(np.exp(arr))

# Checking data in dS(Same as arr):
# if 1 in arr
# print(9 in arr)



# Dictionary in arr:
sdata = {'Lahore':3500,'Karachi':24234,'Islamabad':32424}
DictSeries=pd.Series(sdata)
# print(DictSeries)

# Another way:
data=[4345,4353,6875,2345]
cities=['lhr','khi','isb','pwr']

NewDict = pd.Series(data,index=cities)
# print(NewDict)

# Or:
labelsStd = ['name', 'Rollno', 'Degree']

Students = {
    1: {'name': 'Ali', 'Rollno': '21F-9502', 'Degree': 'CS'},
    2: {'name': 'Asad', 'Rollno': '22L-9583', 'Degree': 'SE'},
    3: {'name': 'Sarah', 'Rollno': '23I-9472', 'Degree': 'CS'},
    4: {'name': 'Ayesha', 'Rollno': '18P-3843', 'Degree': 'EE'}
}

StdDict = pd.Series(data=Students)
# print(StdDict)
# pd.isnull(StdDict)


##DataFrame:


list = np.array([1.5,1.7,3.6,2.4,2.9])

data={
        'state': ['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year': [2000,2001,2002,2001,2002],
        'pop': list
     }

# dataDF=pd.DataFrame(data)
#print (dataDF)
# dataDF

# Passing column sequence and custom indexes:
dataDF=pd.DataFrame(data,columns=['year','state','pop'],index=['cero','uno','dos','tres','quattro'])
dataDF
# If a non-existing column is passed in sequence,
# N/A is returned

# Accessing single column:
dataDF.year

# Accessing single row:
row_data = dataDF.loc['uno']

# Using conditionals:
dataDF[dataDF['year']==2001]

# Adding new col:
dataDF['debt'] = [16.5,1,None,3,4]

# Deleting a column:
# del dataDF['debt']
dataDF


# # Deleting a row:

# dataDF.drop(0)

# Transpose:
# dataDF.T

# Re index and create new data frame
newDF = dataDF.reindex(columns=['year','state','debt','pop'],index=['dos','cero','uno','quattro','tres'])
newDF

# Applying functions on dictionaries:
def func(x):
    x = x - 1
    return x

print(func(dataDF['year']))


# Extra functions:
# Sorting (rows) i.e. c from cero, d from dos, q from quattro:
newSortedDF = dataDF.sort_index(axis=0)
# To Sort current df instead of creating new one:
# dataDF.sort_index(axis=0,inplace=True)

# To sort columns:
dataDF.sort_values('pop')

# Describe gices all functions:
dataDF.describe()

# Applying these:

# Aggregation	Description
# count()	Total number of items
# mean(), median()	Mean and median
# min(), max()	Minimum and maximum
# std(), var()	Standard deviation and variance
# mad()	Mean absolute deviation
# prod()	Product of all items
# sum()	Sum of all items

# These are all methods of DataFrame and Series objects.

dataDF['pop'].max()
dataDF.max()

# Handle missing data: put none or np.nan
# data = pd.Series([ "Umman", np.nan,"Samad", None])
# data 

# Filter numeric columns
numeric_columns = dataDF.select_dtypes(include=[np.number])

# Group by 'year' and apply aggregate functions to numeric columns
result = numeric_columns.groupby('year').agg(['min', np.median, 'max'])

print(result)



# Read from file:
pdData = pd.read_csv('C:\\Users\\MOIZ UDDIN\\Desktop\\Python\\Labs & project\\Labs & project\\historical_stock_prices.csv')

DataDF = pdData.to_dict(orient='list')

df_from_dict = pd.DataFrame(DataDF)

df_from_dict
