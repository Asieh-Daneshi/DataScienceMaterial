import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as pplt
import seaborn as SNS
# =============================================================================
sales=pd.read_csv("sales_data.csv")
sales.shape         # it is like "size" in MATLAB
sales.describe()        # descriptive statistics about dataframe
sales["Unit_Cost"].describe()       # descriptive statistics only for column "Unit_Cost" 
sales["Unit_Cost"].mean()
sales["Unit_Cost"].median()
sales["Unit_Cost"].plot(kind="box", vert=False, figsize=(12,3))
pplt.figure(figsize=(12,3))
pplt.boxplot(sales["Unit_Cost"], positions=[2], widths=0.1, patch_artist=True, vert=False)
#                 showmeans=False, showfliers=False,
#                 medianprops={"color": "white", "linewidth": 0.5},
#                 boxprops={"facecolor": "C0", "edgecolor": "white",
#                           "linewidth": 0.5},
#                 whiskerprops={"color": "C0", "linewidth": 1.5},
#                 capprops={"color": "C0", "linewidth": 1.5})
sales["Unit_Cost"].plot(kind="density", figsize=(6,3))
sales["Unit_Cost"].plot(kind="hist", figsize=(6,3), color=(1,0,0), edgecolor=[0,0,0])
sales["Age_Group"].value_counts().plot(kind="pie", colors=[(1,1,0),(0,1,0),(1,0,0),(0,0,1)],figsize=(6,6))
sales["Age_Group"].value_counts().plot(kind="bar",figsize=(12,6))

# Here, I want to see how correlated two features of my data are. 
Sales=sales
Sales=Sales.drop(["Date", "Month", "Age_Group", "Customer_Gender", "Country", "State", "Product_Category", "Sub_Category", "Product"],  axis = 1)
corr=Sales.corr()           # correlation matrix
pplt.matshow(corr,cmap='RdBu')
# How "profit" is correlated to "Revenue"?
sales.plot(kind="scatter", x="Revenue", y="Profit", figsize=(6,6))

m, b =np.polyfit(sales["Revenue"],sales["Profit"],1)
# plt.pyplot.plot(sales["Revenue"],sales["Profit"],'yo',sales["Revenue"],m*sales["Revenue"]+b,'--k')
plt.pyplot.plot(sales["Revenue"],m*sales["Revenue"]+b,'--k')

cov=Sales.cov()           # covariance matrix
pplt.matshow(cov,cmap='RdBu')
# Reminder:
# Corr(Xi , Xj)= Cov(Xi , Xj)/(σXi * σXj)
sales["Unit_Price"]+=1              # increasing the values in the "Unit_Price" column by 1
sales.iloc[0]                       # address specific row (here 0)
sales.loc[sales["Country"] == "Canada" , "Unit_Price"]+=1           # address specific labels (here "Canada") in a specific column (here "Unit_Price")
 
​

​
