import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('world_happiness_report_alter.csv')

# print(df['Regional indicator'].unique()), wanted each one on a new line so used code below instead
print(df['Regional_Indicator'].value_counts().sort_index())
print('--'*30)
print(df.value_counts(['Regional_Indicator','Ladder_Category']).sort_index())

print(df['Ladder_Category'].value_counts())
print(df.loc[df['Ladder_Category'] == 'Suffering'])
print('--'*30)


def RegCalc(column):
        return(df.groupby('Regional_Indicator', as_index=False).agg({column:['min','max','mean']}).round(3))

#not sure if its bad practice to use spaces between apostrophes eg ' while ' or to use + ' ' +
#struggled with this one to figure out how to return a single value and its corresponding country 
#ended up with with code below

def CountryCalc(column):
        var=df.iloc[df[column].idxmax()]
        var1=df.iloc[df[column].idxmin()]
        return(var[0] +' scored highest in '+ column +' while '+ var1[0] +' scored lowest in '+ column)


df_calc = df.iloc[:,[2,6,7,8,9,10,11]]

for x in df_calc:
        print(RegCalc(x))

print('--'*30)
print(CountryCalc('Ladder_Score'))
print(CountryCalc('Logged_GDPper_Capita'))
print('--'*30)

# Want to print correlation between Ladder_Score and the rest of the relevant columns
#Method one: 
        #df.corr(method='pearson')
        #the whole dataframe against each other, but i only want Ladder_score against the selected columns
#Method two: 
        #corr_df2 = df.iloc[:,6:]
        #corr_df = df['Ladder_Score']
        #correlation=corr_df.corrwith(corr_df2, axis = 1) tried axis=0 also
        #print(correlation)
        #AttributeError: 'Series' object has no attribute 'corrwith', corrwith is for two dataframes
#Method 3
        #correlation=df['Ladder_Score'].corr(df[6:], method='pearson') 
        #ValueError: operands could not be broadcast together with shapes (143,) (143,20)
#Method 4: print relevant columns

df_1 = df.iloc[:,6:12]
df_ls = df_1.corrwith(df['Ladder_Score'])
print('Correlation coefficient of Ladder Score with columns below:\n', df_ls)




