import pandas as pd
import click
@click.command()
@click.option('-i','--input',help = "Input file is a list file, of which each line containing an absolute/relative address of a file including 2 columns: col1 is Gene_id, col2 is count number without header.")
@click.option('-o','--output', default = 'merge.txt', help = 'Output file containing Gene_id and count number in every single sample.')
@click.option('-c','--colname', help = 'File each line containing the name of each sample.')
@click.option('-f','--feature_name', default = 'gene_id', help = "Name of feature you concerned about, which will be outputed as name of the fitse column of the output file.")

def main(input, output, colname, feature_name):
	b = pd.read_table(f"{input}", header=None)
	tcolumns = pd.read_table(f"{colname}", header = None)
	for i in range(b.shape[0]) :
		tcolname = tcolumns.iloc[i,0]
		if i == 0:
			table = pd.read_table(f"{b.iloc[i,0]}", header = None, sep='\t') 
			table.columns = [feature_name,tcolname]
		else:
			table2 = pd.read_table(f"{b.iloc[i,0]}", header = None, sep='\t')
			table2.columns = [feature_name,tcolname]
			table = pd.merge(table,table2,how='inner', on=f"{feature_name}")
		table2 = 0
	table.to_csv(f"{output}",sep="\t",index=False)
if __name__ == '__main__':
    main()
