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
