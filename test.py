import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('world_happiness_report_alter.csv')
df_1 = df.iloc[:,6:12]
df_2 = df.iloc[:,2:3]
df_corr = pd.concat([df_1 , df_2], axis=1)

def RegCalc(column):
        return(df.groupby('Regional_Indicator', as_index=False).agg({column:['min','max','mean']}).round(3))

#not sure if its bad practice to use spaces between apostrophes eg ' while ' or to use + ' ' +
#struggled with this one to figure out how to return a single value and its corresponding country 
#ended up with with code below
for x in df_corr:
    print(RegCalc(x))

