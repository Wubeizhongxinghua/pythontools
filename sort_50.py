import pandas as pd
import click
@click.command()
@click.option('-i','--input',help="Input file")
@click.option('-o','--output',help="Output file")


def main(input,output):
	df = pd.read_table(input)
	df["mean"] = df.iloc[:,1:].mean(axis=1)
	df.sort_values(by="mean",inplace=True,ascending=False)
	df.to_csv(output,index=False,sep="\t")

if __name__ == '__main__':
	main()
