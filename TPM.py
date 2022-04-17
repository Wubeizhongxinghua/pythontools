import pandas as pd
import numpy as np
import click
@click.command()
@click.option('-i','--input',help = 'Input count matrix')
@click.option('-o','--output', help = 'Output TPM matrix')
@click.option('-l','--length', help = 'Length of every element')
@click.option('-f','--feature', help = 'Feature name')
def main(input,output,length,feature):
	df = pd.read_table(f"{input}",header=None)
	length = pd.read_table(f"{length}",header=None)
	dl = pd.merge(left=df,right=length,left_on=feature, right_on ="gene")
	RPK = dl.iloc[:,1:-2].div(dl.iloc[-1],axis = 0)
	tRPK = RPK.sum(axis=0)
	TPM = RPK.div(tRPK,axis = 1)
	TPM.to_csv(f"{output}",sep="\t")

if '__name__'=='__main__':
	main()
