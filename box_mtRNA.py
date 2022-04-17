import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mtRNA=['ENSG00000198888',
       'ENSG00000198763',
       'ENSG00000198840',
       'ENSG00000212907',
       'ENSG00000198886',
       'ENSG00000198786',
       'ENSG00000198695',
       'ENSG00000198727',
       'ENSG00000198804',
       'ENSG00000198712',
       'ENSG00000198938',
       'ENSG00000198899',
       'ENSG00000228253',
       #'ENSG00000211459',
       #'ENSG00000210082',
       'ENSG00000210127',
       'ENSG00000210174',
       'ENSG00000210135',
       'ENSG00000210154',
       'ENSG00000210140',
       'ENSG00000210194',
       'ENSG00000210107',
       'ENSG00000210164',
       'ENSG00000210176',
       'ENSG00000210100',
       'ENSG00000209082',
       'ENSG00000210191',
       'ENSG00000210156',
       'ENSG00000210112',
       'ENSG00000210049',
       'ENSG00000210196',
       'ENSG00000210151',
       'ENSG00000210184',
       'ENSG00000210195',
       'ENSG00000210117',
       'ENSG00000210144',
       'ENSG00000210077']
mtRNA_new=[
    'ENST00000387314.1|ENSG00000210049.1|-|-|MT-TF-201|MT-TF|71|Mt_tRNA|',
    'ENST00000389680.2|ENSG00000211459.2|-|-|MT-RNR1-201|MT-RNR1|954|Mt_rRNA|',
    'ENST00000387342.1|ENSG00000210077.1|-|-|MT-TV-201|MT-TV|69|Mt_tRNA|',
    'ENST00000387347.2|ENSG00000210082.2|-|-|MT-RNR2-201|MT-RNR2|1559|Mt_rRNA|',
    'ENST00000386347.1|ENSG00000209082.1|-|-|MT-TL1-201|MT-TL1|75|Mt_tRNA|',
    'ENST00000361390.2|ENSG00000198888.2|-|-|MT-ND1-201|MT-ND1|956|protein_coding|',
    'ENST00000387365.1|ENSG00000210100.1|-|-|MT-TI-201|MT-TI|69|Mt_tRNA|',
    'ENST00000387372.1|ENSG00000210107.1|-|-|MT-TQ-201|MT-TQ|72|Mt_tRNA|',
    'ENST00000387377.1|ENSG00000210112.1|-|-|MT-TM-201|MT-TM|68|Mt_tRNA|',
    'ENST00000361453.3|ENSG00000198763.3|-|-|MT-ND2-201|MT-ND2|1042|protein_coding|',
    'ENST00000387382.1|ENSG00000210117.1|-|-|MT-TW-201|MT-TW|68|Mt_tRNA|',
    'ENST00000387392.1|ENSG00000210127.1|-|-|MT-TA-201|MT-TA|69|Mt_tRNA|',
    'ENST00000387400.1|ENSG00000210135.1|-|-|MT-TN-201|MT-TN|73|Mt_tRNA|',
    'ENST00000387405.1|ENSG00000210140.1|-|-|MT-TC-201|MT-TC|66|Mt_tRNA|',
    'ENST00000387409.1|ENSG00000210144.1|-|-|MT-TY-201|MT-TY|66|Mt_tRNA|',
    'ENST00000361624.2|ENSG00000198804.2|-|-|MT-CO1-201|MT-CO1|1542|protein_coding|',
    'ENST00000387416.2|ENSG00000210151.2|-|-|MT-TS1-201|MT-TS1|69|Mt_tRNA|',
    'ENST00000387419.1|ENSG00000210154.1|-|-|MT-TD-201|MT-TD|68|Mt_tRNA|',
    'ENST00000361739.1|ENSG00000198712.1|-|-|MT-CO2-201|MT-CO2|684|protein_coding|',
    'ENST00000387421.1|ENSG00000210156.1|-|-|MT-TK-201|MT-TK|70|Mt_tRNA|',
    'ENST00000361851.1|ENSG00000228253.1|-|-|MT-ATP8-201|MT-ATP8|207|protein_coding|',
    'ENST00000361899.2|ENSG00000198899.2|-|-|MT-ATP6-201|MT-ATP6|681|protein_coding|',
    'ENST00000362079.2|ENSG00000198938.2|-|-|MT-CO3-201|MT-CO3|784|protein_coding|',
    'ENST00000387429.1|ENSG00000210164.1|-|-|MT-TG-201|MT-TG|68|Mt_tRNA|',
    'ENST00000361227.2|ENSG00000198840.2|-|-|MT-ND3-201|MT-ND3|346|protein_coding|',
    'ENST00000387439.1|ENSG00000210174.1|-|-|MT-TR-201|MT-TR|65|Mt_tRNA|',
    'ENST00000361335.1|ENSG00000212907.2|-|-|MT-ND4L-201|MT-ND4L|297|protein_coding|',
    'ENST00000361381.2|ENSG00000198886.2|-|-|MT-ND4-201|MT-ND4|1378|protein_coding|',
    'ENST00000387441.1|ENSG00000210176.1|-|-|MT-TH-201|MT-TH|69|Mt_tRNA|',
    'ENST00000387449.1|ENSG00000210184.1|-|-|MT-TS2-201|MT-TS2|59|Mt_tRNA|',
    'ENST00000387456.1|ENSG00000210191.1|-|-|MT-TL2-201|MT-TL2|71|Mt_tRNA|',
    'ENST00000361567.2|ENSG00000198786.2|-|-|MT-ND5-201|MT-ND5|1812|protein_coding|',
    'ENST00000361681.2|ENSG00000198695.2|-|-|MT-ND6-201|MT-ND6|525|protein_coding|',
    'ENST00000387459.1|ENSG00000210194.1|-|-|MT-TE-201|MT-TE|69|Mt_tRNA|',
    'ENST00000361789.2|ENSG00000198727.2|-|-|MT-CYB-201|MT-CYB|1141|protein_coding|',
    'ENST00000387460.2|ENSG00000210195.2|-|-|MT-TT-201|MT-TT|66|Mt_tRNA|',
    'ENST00000387461.2|ENSG00000210196.2|-|-|MT-TP-201|MT-TP|68|Mt_tRNA|'
]
longRNA_list=['tucpRNA', 'lncRNA', 'Y_RNA', 'snRNA', 'pseudogene', 'Mt_tRNA', 'srpRNA', 'snoRNA', 'mRNA','circRNA','Mt_tRNA','protein_coding']
mtRNA_type=['Mt_tRNA','Mt_rRNA','protein_coding']

mtRNA_feature=pd.DataFrame(columns={'feature','gene_id'})
mtRNA_feature['feature']=mtRNA_new
mtRNA_feature['gene_id']=mtRNA_feature['feature'].map(lambda x:x.split('|')[1].split('.')[0])

data=pd.read_csv('/BioII/lulab_b/liuxiaofan/project/expanel/HCC/pico/count_matrix/exp_mtRNA_TMM.txt',sep='\t')
gene_all=list(data['feature'])
sample=list(data.columns[1:])
data_long=data.loc[data.feature.isin(list(set(gene_all)-set(mtRNA))),:]
data_mtRNA=data.loc[data.feature.isin(list(set(mtRNA))),:]
data_mtRNA=data_mtRNA.rename(columns={'feature':'gene_id'})
data_mtRNA=pd.merge(data_mtRNA,mtRNA_feature,on='gene_id',how='left')

data_all=pd.concat([data_long,data_mtRNA])
data_all['ID']=data_all['feature'].map(lambda x:x.split('|')[1] if x.split('|')[-2] in mtRNA_type else x.split('|')[0])
data_all['ID_name']=data_all['feature'].map(lambda x:x.split('|')[-5] if x.split('|')[-2] in mtRNA_type else x.split('|')[2])
data_all['type']=data_all['feature'].map(lambda x:x.split('|')[-2] if x.split('|')[-2] in mtRNA_type else x.split('|')[1])
# data_all=data_all.loc[data_all.type.isin(longRNA_list)]


data_median=data_all[sample].median(axis=1)
data_median.index=data_all['ID_name']
data_median=data_median.sort_values(ascending=False)
ID_select=list(data_median.index)[:50]
data_all=data_all.set_index('ID_name')

data_selet=data_all.loc[ID_select,sample]
data_selet=data_selet.T

data_plot=data_selet[[data_selet.columns[0]]]
data_plot.columns=['data']
data_plot['ID_name']=data_selet.columns[0]
for i in list(data_selet.columns[1:]):
    data_=data_selet[[i]]
    data_.columns=['data']
    data_['ID_name']=i
    data_plot=pd.concat([data_plot,data_])

data_median_select=pd.DataFrame(data_median[ID_select]).reset_index()

plt.figure(figsize=(15,10))
sns.axes_style({'font.family': ['sans-serif'],'font.sans-serif': ['Arial']})
ID_select_color=['tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'lightgrey', 'tab:red', 'tab:red', 'tab:red',
                'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'tab:red', 'lightgrey', 'tab:red', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 
                'lightgrey', 'tab:red', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey',
                'lightgrey', 'lightgrey', 'lightgrey', 'tab:red', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 
                'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'tab:red', 'lightgrey']
    
ax=sns.boxplot(x="ID_name", y='data', data=data_plot,order=ID_select,
               palette=ID_select_color,linewidth=2,width=0.8)
plt.setp(ax.lines, color=".3")
# mybox = ax.artists[2]
# mybox.set_facecolor('tab:red')
# mybox.set_edgecolor('black')
# mybox.set_linewidth()
plt.scatter(list(data_median_select['ID_name']),list(data_median_select[0]), color='.3',s=30)
plt.plot(list(data_median_select['ID_name']),list(data_median_select[0]), color='.3',alpha=1,linewidth=3)

ax.spines['right'].set_visible(False) #去掉右边框
ax.spines['top'].set_visible(False) #去掉上边框
ax.spines['bottom'].set_linewidth(2)###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2)####设置左边坐标轴的粗细


font2 = {'family':'Arial','fontweight':'bold','size': 25}
ax.tick_params(width=2,length=5)
plt.ylabel('TMM',font2)
plt.xlabel('')
plt.yticks(fontproperties ='Arial', size = 20,fontweight='bold')
plt.xticks(fontproperties ='Arial', size = 20,fontweight='bold',rotation=90)
for i in range(len(ID_select_color)):
    if ID_select_color[i]=='tab:red':
        plt.gca().get_xticklabels()[i].set_color('tab:red')
plt.tight_layout()
# plt.show()
plt.savefig('/BioII/lulab_b/liuxiaofan/project/expanel/paper/plot_1206/box_mtRNA.png',bbox_inches='tight')
plt.close()
