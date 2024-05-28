import numpy as np
import pandas as pd
dict1 = {
    'name':['st1', 'st2', 'st3'],
    'marks':[8, 7, 6],
    'city':['c1', 'c2', 'c3']
}
df = pd.DataFrame(dict1)
# df.to_html('testWithNoIndex.html', index=False)
# df.to_csv('testWithNoIndexCSV.csv', index=False)
print(df)
print(df.head(2)) # returns the first 2 elements from the top
print(df.tail(2)) # returns the first 2 elements from the bottom
print(df.describe()) # returns count, mean std, etc of numeric  data in a column
usman = pd.read_csv('Book1.csv') # use to read data from a csv file
print(usman) # to print the data read from the file
print(usman['train']) # to print the row that has name train
usman['speed'][0] = 160 # to change the speed value at 0th row
print(usman)
usman.index = ['first', 'second', 'third', 'fourth'] # to change the indexing of dataframe
print(usman)
ser = pd.Series(np.random.rand(20))
print(ser)
newdf = pd.DataFrame(np.random.rand(4, 6), index=np.arange(4))
print(newdf)
print(newdf.index)
print(newdf.to_numpy) # to convert a dataframe in numpy array
print(newdf.T) # to transpose a dataframe
print(newdf.sort_index(axis=1, ascending=False)) # to sort rows in descinding order
newdf2 = newdf # it will make a view(pointer), any change in newdf2 will be reflected in newdf
newdf3 = newdf.copy() # create a copy of newdf on newdf2
newdf.loc[0,0] = 'usman' # to change the value at index 00
print(newdf)
# newdf = newdf.drop(4, axis=1) # to drop the row with heading 4
# print(newdf)
print(newdf)
print(newdf.loc[[2,3],[0, 1]]) # to see desired rows and cols
print(newdf.loc[[2,3],:]) # to see all rows/cols :
print(newdf.iloc[0, 4]) # returns the value w.r.t. index
print(newdf.drop([0, 3], axis=0)) # to drop a row
print(newdf.drop([0, 5], axis=1)) # to drop a column
# print(newdf.drop([0, 5], axis=1, inplace=True)) # to drop a column in the original dataframe
print(newdf.reset_index(drop=True))
print(newdf.isnull()) # returns true if zero is found
newdf.loc[2,:] = None # sets the value to none
print(newdf)