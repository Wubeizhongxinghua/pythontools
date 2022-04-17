import pandas as pd
import click

@click.command()
@click.option('-i','--input',help="Input count matrix")
<<<<<<< HEAD
@click.option('-i','--input',help='Output CPM matrix')
=======
@click.option('-o','--output',help='Output CPM matrix')
>>>>>>> 5bd8b11986f99395b25c9a34d31c0529548a8685

def main(input, output):
	em = pd.read_table(input, sep="\t",header=0, index_col=0)
	ct = em.sum(axis=0)
	filterm = em.div(ct,axis=1)*(10**6)
	filterm.to_csv(output,sep="\t")

if __name__ == "__main__":
	main()
