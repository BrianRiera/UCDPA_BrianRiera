import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('world_happiness_report_alter.csv')

world_columns = ['GDP per Capita','Social support','Life expectancy','Freedom','Generosity','Perceptions of corruption','Ladder score']

df_1 = df.iloc[:,6:12]
df_2 = df.iloc[:,2:3]
df_corr = pd.concat([df_1 , df_2], axis=1)


sns.heatmap(df_corr.corr(),annot=True,linewidths=.5,cmap='coolwarm',
        xticklabels=world_columns, yticklabels=world_columns)
plt.xticks(rotation=90) 
plt.yticks(rotation=0) 
plt.title('Correlation Heatmap', fontsize =20)
plt.tight_layout() # this one line took me about 2 hours, could not figure out how to not cut off my x and yicklabels
plt.savefig('Heatmap.png')
plt.show()


def reg_dist(column):
    g=sns.catplot(x=column,  y='Regional_Indicator', data=df,kind='box',palette='husl',
            showmeans=True,
            meanprops={'marker':'o',
                       'markerfacecolor':'white', 
                       'markeredgecolor':'black',
                      'markersize':'5'})
    g.fig.set_size_inches(12,6)
    g.fig.suptitle('Comparing distribution by Region',weight='bold')
    g.set(xlabel=column,ylabel='Region')
    plt.tight_layout()
    plt.show()

for x in df_corr:
    print(reg_dist(x))

sns.set()  
pair_g=sns.pairplot(data=df, x_vars=['Ladder_Score', 'Logged_GDPper_Capita']
            ,y_vars=['Social_Support', 'Healthy_Life_Expectancy']
            ,hue='Regional_Indicator',palette='husl',diag_kind=None)
             #if i dont put diag_kind=None there are two blank grids
pair_g.fig.set_size_inches(12,6)
pair_g.fig.suptitle('Comparing the relationships across Happiness, GDP, Social Support; and Life Expectancy',y=1,weight='bold')


sns.set()
g=sns.pairplot(data=df,
             vars=['Freedom_Make_Life_Choices', 'Ladder_Score'],
             kind='scatter',
             palette='husl',
             diag_kind ='kde',
             hue='Regional_Indicator')   
g.fig.set_size_inches(12,6)    
g.fig.suptitle('Freedom and Happiness', weight='bold',y=1,)
plt.show()

sns.set_style('ticks')
df['Pop_2020'] = df['Pop_2020'].div(1000000)
l_gdp=sns.regplot(x='Ladder_Score',y='Logged_GDPper_Capita',data=df,
            scatter_kws={'s': df['Pop_2020'],'color':'g','alpha':0.8},
            line_kws={'color':'g'})
l_gdp.set(xlabel='Ladder Score', ylabel='GDP per Capita',xlim=(2,8),ylim=(6,12))
plt.title('GDP and Happiness', fontsize =16, weight='bold',y=1)
plt.tight_layout()


plt.show()

