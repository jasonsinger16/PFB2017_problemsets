#!/usr/bin/env python3

# Write a python program that reads in the 'bowtie2.sam' file and generates a table containing the number of reads mapped to each gene

import sys

input_filename = sys.argv[1]
fh = open(input_filename, "r")

gene_reads = {}
for line in fh:
    line = line.rstrip()
    exploded_line = line.split("\t")
    gene = (exploded_line[2].split("^"))[0]
    read = exploded_line[0]
    if gene not in gene_reads:
        gene_reads[gene]=set()
    gene_reads[gene].add(read)
#print(gene_reads)

formatting_dict = {}
for tallied_gene in gene_reads:
    name = tallied_gene
    tally = len(gene_reads[tallied_gene])
    formatting_dict[name]=tally
#print(formatting_dict)

final_product = sorted(formatting_dict.items(), key=lambda formatting_dict: formatting_dict[1], reverse = True)
#print(final_product)

text = "Gene: {}\t\tNumber of reads: {}"
print()
for gene_name, read_count in final_product:
    print(text.format(gene_name, read_count))
print()

fh.close()
