import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('world_happiness_report_alter.csv')

print(df.columns)
print(df.isnull().sum())




# plt.scatter('Ladder_Score', 'Logged_GDPper_Capita', s='Pop_2020',alpha=0.5, data=df)
# plt.xlabel("X", size=16)
# plt.ylabel("y", size=16)
# plt.title("Bubble Plot with Colors: Matplotlib", size=18)
# plt.show()


#sns.relplot(x=df.Ladder_Score, y=df.Logged_GDPper_Capita, hue=df.Regional_Indicator,kind='scatter',size=df.Pop_2020, style=df.Ladder_Category,alpha=0.5)
#plt.show()

# sns.relplot(x=df.Ladder_Score, y=df.Healthy_Life_Expectancy, hue=df.Regional_Indicator,kind='line', style=df.Regional_Indicator,markers=True,dashes=False)
# plt.show()
# hue_colours = {'Central and Eastern Europe':           
# 'Commonwealth of Independent States':    
# 'East Asia':                             
# 'Latin America and Caribbean':           
# 'Middle East and North Africa':          
# 'North America and ANZ'                  
# 'South Asia':                           
# 'Southeast Asia':                         
# 'Sub-Saharan Africa':                   
# 'Western Europe':      
                  
# plt.figure(figsize=(10,6))
# # make barplot and sort bars in descending order
# sns.barplot(x='Education', 
#             y="Salary", 
#             data=df, 
#             order=df.sort_values('Salary',ascending = False).Education)
# # set labels
# plt.xlabel("Education", size=15)
# plt.ylabel("Salary in US Dollars", size=15)
# plt.title("Sort Bars in Barplot in Descending Order", size=18)
# plt.tight_layout()
# plt.savefig("sort_bars_in_barplot_descending_order_Seaborn_Python.png", dpi=100)


# https://datavizpyr.com/how-to-make-simple-facet-plots-with-seaborn-catplot-in-python/
sns.set_palette
sns.set_style('ticks')
g=sns.catplot(x='Regional_Indicator',  y='Logged_GDPper_Capita', kind='box', data=df,whis=[0,100])
g.fig.suptitle('Comparing GDP by Region',y=1.03)
g.set(xlabel='Region',ylabel='GDP')
plt.xticks(rotation=90)

#need to change size
# sns.catplot(x='',  y='Logged_GDPper_Capita', kind='bar', data=df)
sns.lmplot(x='Ladder_Score',y='Logged_GDPper_Capita',data=df)


# sns.stripplot(data=df, y='Regional_Indicator',x='Healthy_Life_Expectancy')



# sns.catplot(x='Regional_Indicator',  y='Logged_GDPper_Capita',kind='swarm',data=df)
# plt.show()

#Tried a load of different things to try and shape this so that it wouldnt cut off my labels and this is what i ended up with
#cant add legend with heatmap for labels, tried g.figure.tight_layout(), adjusting limits etc,sns.set_context
labels = ['GDP per Capita(GDP)','Social support(SS)','Life expectancy(LE)','Freedom(F)','Generosity(G)','Perceptions of corruption(PC)','Ladder score(LS)']
labels_abbrev =['GDP','SS','LE','F','G','PC','LS']
print(df.columns)
plt.figure(figsize=(20,20))
df_1 = df.iloc[:,6:12]
df_2 = df.iloc[:,2:3]
df_corr = pd.concat([df_1 , df_2], axis=1)
sns.heatmap(df_corr.corr(),annot=True,linewidths=.5,cmap='coolwarm',xticklabels=labels_abbrev, yticklabels=labels)
plt.xticks(rotation=0) 
plt.yticks(rotation=0) 
plt.title('Pearson Correlation', fontsize =20)
plt.savefig('Heatmap.png')
plt.show()
#change colour and fix other things
#center = df_crosstab.loc[9,6]