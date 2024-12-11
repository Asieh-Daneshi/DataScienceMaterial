import numpy as np
import pandas as pd
data = {'Name': ['Marcel_Brass',
                 'Asieh Daneshi',
                 'Yu_Hei_Shum?'],
        'Pos': ['Principal Investigator',
                'Postdoctoral Research Fellow',
                'PhD Student']}
df = pd.DataFrame(data)
Names = df['Name'].str.split('_')   # splits the column 'Name' based on '_' signs, and put each part in a separate column
NamesDF = df['Name'].str.split('_',expand=True)     # adding "expand=True" turns the output to dataframe
df['Name'].str.contains('a')    # looking for a specific character in our dataframe
# Note: if we are looking for "?" in our dataframe, we should write "\?"
df['Name'].str.contains('\?')

df['Name'].str.strip('a')       # removes the specific character from the strip
df['Name'].str.replace(' ','')  # replaces the first specified character with the second one

