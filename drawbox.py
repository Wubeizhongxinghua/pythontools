import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_table("TPMf_GSE123972.txt").fillna(0)
dfv = df.iloc[:,:-1]
dfd = pd.DataFrame(dfv.values.T, index=dfv.columns, columns = dfv.index)
new_header = dfd.iloc[0] #grab the first row for the header
dfd = dfd[1:] #take the data less the header row
dfd.columns = new_header #set the header row as the df header
mtRNA = pd.read_table("mtRNA_name_2")
ax=sns.boxplot(data=dfd,linewidth=2,width=0.8)
plt.scatter(list(df.iloc[:,0]),list(df["mean"]), color='.3',s=30)
plt.plot(list(df.iloc[:,0]),list(df["mean"]), color='.3',alpha=1,linewidth=3)
font2 = {'family':'Arial','fontweight':'bold','size': 25}
ax.tick_params(width=2,length=5)
plt.ylabel('TPM',font2)
plt.xlabel('')
plt.yticks(fontproperties ='Arial', size = 20,fontweight='bold')
plt.xticks(fontproperties ='Arial', size = 20,fontweight='bold',rotation=90)
for i in range(1,df.shape[0]):
    if dfd.columns[i] in list(mtRNA.iloc[:,0]):
        plt.gca().get_xticklabels()[i].set_color('tab:red')
plt.tight_layout()
plt.show()
