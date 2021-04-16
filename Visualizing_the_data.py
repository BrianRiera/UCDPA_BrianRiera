import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('world_happiness_report_alter.csv')


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

#g=sns.catplot(x='Regional_Indicator',  y='Logged_GDPper_Capita', kind='box', data=df,whis=[0,100])
#g.fig.suptitle('Comparing GDP by Region',y=1.03)
#g.set(xlabel='Region',ylabel='GDP')
#plt.xticks(rotation=90)

#need to change size
# sns.catplot(x='',  y='Logged_GDPper_Capita', kind='bar', data=df)
#maybe just use a normal scatter plot
#sns.set(color_codes=True)
#sns.palplot(sns.color_palette('Purples', 10))


#Fit a higher-order polynomial regression: look into this

df['Pop_2020'] = df['Pop_2020'].div(1000000)
sns.set_style('ticks')
sns.set(font_scale= 1.5)
g=sns.regplot(x='Ladder_Score',y='Logged_GDPper_Capita',data=df,scatter_kws={'s': df['Pop_2020'],'color':'purple','alpha':0.8},line_kws={'color':'m'})
g.set(xlabel='Ladder Score', ylabel='GDP per Capita',xlim=(2,8),ylim=(6,12))
plt.title('Happiness & GDP', fontsize =20, weight='bold',y=1)
plt.tight_layout()
plt.savefig('HappinessVsGDP.png')
plt.show()
plt.clf()

