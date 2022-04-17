import pandas as pd
import click

@click.command()
@click.option('-i','--input',help="Input count expression matrix")
@click.option('-o','--output',help='Output expression matrix filtered.')
@click.option('-t','--threshold',default = 0.5, help="Filtering threshold\n default: CPM>0.5")
@click.option('-l','--at_least',default = 1, help="A specific gene will not be removed only if the number of samples that the CPM of the gene is lerger than the threshold you set is over the value you set at this option.\n default:1")

def main(input,output,threshold,at_least):
	em = pd.read_table(f"{input}",sep="\t",header=0,index_col=0)
	ct = em.sum(axis=0)
	filterm = em.div(ct,axis=1)*(10**6)
	print(filterm)
	raw = []
	for i in range(filterm.shape[0]):
		c = 0
		for t in range(filterm.shape[1]):
			if filterm.iloc[i,t] >= threshold:
				c += 1
			if c >= at_least:
				raw.append(i)
				break
	out = em.iloc[raw,:]
	out.to_csv(f"{output}",sep="\t")
if __name__== '__main__':
	main()
