import pandas as pd

df=pd.read_csv('world-happiness-report-2021.csv')
pop = pd.read_csv('population_by_country_2020.csv')
print(df.head(5))
print(df.shape)
print(df.info())

print('--'*30)

print(pop.head(5))
print(pop.shape)
print(pop.info())

pop_1 = pop.iloc[:,:2] #only want population column
pop_df = pd.merge(df, pop_1, how='left', left_on='Country name', right_on='Country (or dependency)')
pop_df_alter = pop_df.drop(columns='Country (or dependency)')

df1=pop_df_alter.sort_values('Country name', ascending = True).reset_index(drop=True)
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
                    'Dystopia + residual':'Dystopia_Residual',
                    'Population (2020)':'Pop_2020'},inplace=True)
# For duplicate/missing values to drop/fill
# With missing numeric values the alternative options i would've considered are below:
# new_df.fillna(new_df.mean(), inplace=True) or a forward/back fill but think it would be better to drop in this context 
# new_df2 = new_df.drop_duplicates(subset['column_name1'])
#df['column name'] = df['column name'].replace(['1st old value','2nd old value',...],
# ['1st new value','2nd new value',...])

print(df1.isnull().sum())
df1.dropna(subset = ['Pop_2020'], inplace=True)

#to check if changes worked properly
print('--'*30)
print(df1.head(2))
print(df1.shape)
print('--'*30)


print('--'*30)
df1['Ladder_Category'] = None
for idx, row in df1.iterrows():
        if row['Ladder_Score'] <= 3.333:
                df1.loc[idx, 'Ladder_Category'] = 'Suffering'
        elif row['Ladder_Score'] <=6.666:
                df1.loc[idx, 'Ladder_Category'] = 'Struggling'
        else:
                df1.loc[idx, 'Ladder_Category'] = 'Thriving'

#just wanted to see each one on new line in code below to make easier to check changes to column names
for i in df1.columns:
        print(i)
print(df1.isnull().sum())
df1.to_csv(r'C:\Users\User\Documents\GitHub\UCDPA_BrianRiera\world_happiness_report_alter.csv', index = False)

