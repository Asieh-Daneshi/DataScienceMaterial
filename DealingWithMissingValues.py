import numpy as np
import pandas as pd
toyArray = np.arange(1,100,1)
toyArrayMissing = np.array(toyArray, dtype=np.float16)
toyArrayMissing[[1,4,7]]=np.nan

# =============================================================================
pd.isnull(np.nan)
pd.isnull(None)           # None is like "np.nan", but I use np.nan from now on
pd.isnull(toyArrayMissing[0])
pd.isnull(toyArrayMissing[1])
pd.isna(toyArrayMissing[0])                       # isna is exactly like isnull
pd.isna(toyArrayMissing[1])
pd.isnull(toyArrayMissing)                   # checks all the elements in array
pd.isnull(toyArrayMissing).sum()                # counts all the missing values
pd.notnull(toyArrayMissing).sum()            # counts all the nonmissing values
toyArrayMissing = toyArrayMissing[pd.notnull(toyArrayMissing)]  # removing missing elements from array
# for dataframes we can use dropna to deal with missing values. But, there is something to notice, dropna removes all the data that one value from them is missing. 
# I mean if we have the values for all the parameters, but just one element is missing, the whole row will be removed. That is reasonable, right?
data = {'Roll No': [1, 2, 3, 4, 5],
        'Physics': [90, None, 85, 70, 60],
        'Chemistry': [80, 75, None, 90, 85],
        'Maths': [None, 65, 78, 82, 95],
        'Computers': [None, 80, 72, 88, None]}
df = pd.DataFrame(data)
df.dropna()            # removes all the rows with one or more missing elements
df.dropna(how='any')   # removes all the rows with one or more missing elements
df.dropna(how='all')       # removes the rows that all the elements are missing
df.dropna(thresh=4, axis='rows')  # keeps the rows that at least 4 elementa aren't nan
df.info()
df.isnull().sum()                 # counts number of missing values in each column
df.T.isnull().sum()               # counts number of missing values in each row
df.isnull().sum().sum()           # counts number of missing values in the whole dataframe
df.fillna(0)                      # fills the missing values with zero
df.fillna(df.mean())              # fills the missing values with the mean of dataframe
df.fillna(method='ffill')         # fills the missing values with elements right above them
df.fillna(method='bfill')         # fills the missing values with elements right below them
df.fillna(method='ffill', axis=1)         # fills the missing values with elements left of them (it is actually stupid, because it is replacing missing values of one variable with another variable)
# Note: 'axis=0' is vertical
df.fillna({'Physics':0, 'Chemistry':80, 'Maths':df['Maths'].mean(), 'Computers': df['Computers'].median()})
df['Physics'].value_counts()      # returns the number of each elements in the specified column
df['Physics'].replace(60, 65)     # if a value is invalid, we can replace it 
df.loc[df['Physics']<65]=65       # be careful! this one changes the dataframe
df.duplicated()                   # check for duplicated rows  
df.loc[5] = {'Roll No':65.0,'Physics':65.0,'Chemistry':65.0,'Maths':65.0,'Computers':65.0}      # delibrately duplicate the last row
df.loc[6] = df.loc[2]             # copies third row to the 7th row
df.duplicated()
df.duplicated(subset=['Maths'])   # finds the duplicated elements in column='Maths'
# here I find which row is the original row that 'deplicatedRow' is its copy
deplicatedRow=5
for a in range(0, df.shape[0]):
    n=0
    for b in range(0, df.shape[1]):
        if((df.loc[a][b]==df.loc[deplicatedRow][b]) | (pd.isna(df.loc[a][b]) & pd.isna(df.loc[deplicatedRow][b]))):
            n=n+1
        if(n==df.shape[1] and a!=deplicatedRow):
            print("row: ",a)
