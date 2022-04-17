import pandas as pd
import click

@click.command()
@click.option('-i','--input',help="Input count matrix")
@click.option('-o','--output',help='Output CPM matrix')
def main(input, output):
	em = pd.read_table(input, sep="\t",header=0, index_col=0)
	ct = em.sum(axis=0)
	filterm = em.div(ct,axis=1)*(10**6)
	filterm.to_csv(output,sep="\t")

if __name__ == "__main__":
	main()
