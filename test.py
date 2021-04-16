import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('world_happiness_report_alter.csv')
# df.rename(columns={'Regional_Indicator':'Region',
#                     'Ladder_Score':'Ladder Score',
#                     'Logged_GDPper_Capita':'GDP per Capita',
#                     'Social_Support':'Social support',
#                     'Healthy_Life_Expectancy':'Healthy life expectancy',
#                     'Freedom_Make_Life_Choices':'Freedom to make life choices',
#                     'Perceptions_Corruption':'Perceptions of corruption',
#                     'Ladder_Category':'Ladder Category',
#                     'Pop_2020':'Population 2020'},inplace=True)

labels = ['GDP per Capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption','Ladder score']
print(df.columns)
plt.figure(figsize=(18,10))
df_1 = df.iloc[:,6:12]
df_2 = df.iloc[:,2:3]
df_corr = pd.concat([df_1 , df_2], axis=1)
sns.heatmap(df_corr.corr(),annot=True,linewidths=.5,cmap='YlGnBu',xticklabels=labels, yticklabels=labels)
plt.title('Pearson Correlation', fontsize =20)
plt.show()