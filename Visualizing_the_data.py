import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('world_happiness_report_alter.csv',index_col=['Country_Name'])


print(df.columns)
print(df.isnull().sum())

# fig, ax = plt.subplots()
# # ax.scatter(df['Ladder_Score'],df['Logged_GDPper_Capita'],c=df.Ladder_Score)#ValueError: 'c' argument must be a color, a sequence of colors, or a sequence of numbers, not Country_Name
# # ax.set_xticklabels(df['Ladder_Score'],rotation=90)
# # ax.set_ylabel('GDP')
# # plt.show()
# #fig.savefig(filename.png) as_A_string
# regions = df['Regional_Indicator'].unique()
# for region in regions:
#     region_df = df[df['Regional_Indicator'] == region]
#     ax.bar(region, region_df['Ladder_Score'].mean(),yerr=region_df['Ladder_Score'].std())
# ax.set_ylabel('Ladder score')
# ax.set_xticklabels(regions, rotation=90)
# plt.ylim(ymax = 10, ymin = 0)
# plt.show()



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
                  