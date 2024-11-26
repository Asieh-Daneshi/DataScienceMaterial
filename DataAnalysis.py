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
sales.plot(kind="scatter", x="Revenue", y="Profit", figsize=(6,6))
sales.iloc[1]
