import pandas as pd
import numpy as np


file = 'world-happiness-report-2021.csv'
df=pd.read_csv(file)
print(df.head(5))
print(df.shape)
print(df.info())

# print(df.isna().sum()) already shown no null values in data.info() but included 

# No merging or relevant duplicate/missing values to drop, code below is what i would do:(excuse the lack of imagination for table/variable names)
# new_df = pd.merge(left=df, right=df2, how='left', left_on='Country Name', right_on='Country Column')
# Also with missing numeric values the two options i would've considered are below:
# new_df.fillna(new_df.mean(), inplace=True) but think it would be better to drop in this context 
# new_df.dropna(self, axis=0, how='any', thresh=None, subset=None, inplace=False)
# new_df2 = new_df.drop_duplicates(subset['column_name1'])



df1=df.sort_values('Country name', ascending = True).reset_index(drop=True)
df1.rename(columns={'Country name':'Country_Name',
                     'Regional indicator':'Regional_Indicator',
                    'Ladder score':'Ladder_Score',
                    'Standard error of ladder score':'Standard_Error_Ladder_Score',
                    'upperwhisker':'Upper_Whisker',
                    'lowerwhisker':'Lower_Whisker',
                    'Logged GDP per capita':'Logged_GDPper_Capita',
                    'Social support':'Social_Support',
                    'Healthy life expectancy':'Healthy_Life_Expectancy',
                    'Freedom to make life choices':'Freedom_Make_Life_Choices',
                    'Perceptions of corruption':'Perceptions_Corruption',
                    'Ladder score in Dystopia':'Ladder_Score_Dystopia',
                    'Explained by: Log GDP per capita':'E_Log_GDPper_Capita',
                    'Explained by: Social support':'E_Social_Support',
                    'Explained by: Healthy life expectancy':'E_Healthy_Life_Expectancy',
                    'Explained by: Freedom to make life choices':'E_Freedom_Make_Life_Choices',
                    'Explained by: Generosity':'E_Generosity',
                    'Explained by: Perceptions of corruption':'E_Perceptions_Corruption',
                    'Dystopia + residual':'Dystopia_Residual'},inplace=True)
print(df1.head(2))

for i in df1.columns:
        print(i)
# print(df['Regional indicator'].unique()), wanted each one on a new line so used code below instead
print(df1['Regional_Indicator'].value_counts())

def RegCalc(column):
        return(df1.groupby('Regional_Indicator', as_index=False).agg({column:['min','max','mean']}).round(3))

#not sure if its bad practice to use spaces between apostrophes eg ' while ' or to use + ' ' +
#struggled with this one to figure out how to return a single value and its corresponding country 
#ended up with with code below
def CountryCalc(column):
        var=df1.iloc[df1[column].idxmax()]
        var1=df1.iloc[df1[column].idxmin()]
        return(var[0] +' scored highest in '+column +' while '+var1[0] +' scored lowest in '+column)


print(RegCalc('Ladder_Score'))
print(' ')#for my output readability 
print(RegCalc('E_Log_GDPper_Capita'))
print(CountryCalc('Ladder_Score'))
print(CountryCalc('Social_Support'))