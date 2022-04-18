import pandas as pd
import numpy as np
import click
@click.command()
@click.option('-i','--input',help = 'Input count matrix')
@click.option('-o','--output', help = 'Output TPM matrix')
@click.option('-l','--length', help = 'Length of every element')
@click.option('-f','--feature', help = 'Feature name')
def main(input,output,length,feature):
	df = pd.read_table(f"{input}")
	#df.iloc[:,0] = df.iloc[:,0].astype(object)
	#store = df.iloc[:,0].values.copy()
	df.iloc[:,0] = df.iloc[:,0].str.split("|",expand=True)[0]
	length = pd.read_table(f"{length}")
	#length.iloc[:,0] = length.iloc[:,0].astype(object)
	dl = pd.merge(left=df,right=length,left_on=feature, right_on ="mtRNA")
	RPK = dl.iloc[:,1:-1].div(dl.iloc[:,-1],axis = 0)
	tRPK = RPK.sum(axis=0)
	TPM = RPK.div(tRPK,axis = 1)
	TPM = pd.concat([dl.iloc[:,0],TPM],axis = 1)
	#TPM.iloc[:,0] = store
	TPM.to_csv(f"{output}",sep="\t",index=False)

if __name__=='__main__':
	main()
