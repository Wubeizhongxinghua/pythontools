import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot as plt
import click
@click.command()
@click.option('-i','--input_file', help="Output file of DESeq2, where the first column is numbers instead of names of feature.\t Absolute address is recommanded.\t The file must be filtered according to log2FC and padj")
@click.option('-o','--output_file',default = "./heatmap.svg", help="Heatmap outputfile. \n default: \"./heatmap.svg\"")
@click.option('-d','--dropna',default='1', help="Whether you'd like to delete all rows with NA value and replace the origin file. 1 is yes, other inputs are no. \n default:1")
@click.option('-c','--control', nargs=2,help ="A common character of sample names in control group. If it's the head character, add 0, it not , add -1. \n Example: Names of samples in control group:[\"ct1\",\"ct2\"],then input: c 0")
@click.option('-t','--treat',nargs=2,help="Args for trear group. The detailed description can be seen in \'--control\'")

def main(input_file, output_file, dropna,control,treat):
    list_ids=[]
    list_samples=[]
    list_value_list=[]
    list_sample_colors=[]
    list_gene_colors=[]
    common_control = control[0]
    common_treat = treat[0]
    seq_control = control[1]
    seq_treat = treat[1]
    begin_samples=7
    index_log2FC=2
    index_padj=6
    number_row=1
    if dropna == 1:
        input_file = pd.read_table(f"{input_file}",sep="\t",index_col=0).dropna()
        input_file.to_csv(f"{input_file}",sep="\t")
    for line in open(f"{input_file}"):
        if number_row!=1:
            list_ids.append(line[:-1].split('\t')[1])
            list_value_list_tmp=[]
            index=0
            for value_list in list_value_list:
                value_list.append(float(line[:-1].split('\t')[begin_samples:][index]))
                list_value_list_tmp.append(value_list)
                index+=1
            list_value_list=list_value_list_tmp
            log2FC=float(line[:-1].split('\t')[index_log2FC])
            padj=float(line[:-1].split('\t')[index_padj])
            if padj<0.05 and log2FC>1:
                list_gene_colors.append(sns.color_palette("Set1", n_colors=8, desat=.5)[0])
            if padj<0.05 and log2FC<-1:
                list_gene_colors.append(sns.color_palette("Set1", n_colors=8, desat=.5)[1])

        else:
            begin_samples = line[:-1].split('\t').index('padj') + 1
            index_log2FC = line[:-1].split('\t').index('log2FoldChange')
            index_padj = line[:-1].split('\t').index('padj')
            for sample in line[:-1].split('\t')[begin_samples:]:
                list_samples.append(sample)
                if sample[int(seq_treat)]==common_treat:
                    list_sample_colors.append(sns.color_palette("Set1", n_colors=8, desat=.5)[0])
                if sample[int(seq_control)]==common_control:
                    list_sample_colors.append(sns.color_palette("Set1", n_colors=8, desat=.5)[2])
            for time in range(0,len(line[:-1].split('\t')[begin_samples:])):
                list_value_list.append([])
        number_row+=1

    data=pd.DataFrame(data=list_value_list,index=list_samples,columns=list_ids)
    print(data)
    ax=sns.clustermap(data,standard_scale=1,row_colors=list_sample_colors,col_colors=list_gene_colors,figsize=(19,19))
    plt.savefig(f"{output_file}")
    plt.show()

if __name__ == "__main__":
    main()
