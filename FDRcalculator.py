import pandas as pd
import numpy as np
import click
@click.command()
@click.option('-i','--input')
@click.option('-o','--output')
@click.option('-t','--threshold',default=0.05, help="Providing FDR < threshold, then regarded as significant.\n default:0.05")
def main(input,output,threshold):
	df = pd.read_table(f"{input}",sep="\t",index_col=0,header=0)
	df.sort_values(by='pvalue',inplace=True)
	df['rank'] =np.arange(df.shape[0])+1
	df['FDR'] = df.apply(lambda x : x['pvalue']*df.shape[0]/x['rank'],axis = 1)
	i = df.shape[0]-1
	df['FDR*'] = df['FDR']
	while i >= 0:
		if i != df.shape[0]-1:
			df['FDR*'].iloc[i] = min(df['FDR*'].iloc[i],df['FDR*'].iloc[i+1])
		i -= 1 
	df.to_csv(f'{output}'+'_data.txt',sep="\t")
	df2 = df.loc[df['FDR*']<threshold]
	df2.to_csv(f'{output}'+'_filter.txt',sep='\t')
if __name__== '__main__':
	main()
