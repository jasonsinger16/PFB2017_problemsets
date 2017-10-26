#!/usr/bin/env python3

fasta_file_obj = open("ecoli_6X.fasta", 'r')

counter = 0
for line in fasta_file_obj:
    if line.startswith(">"):
        counter += 1
print("The number of contigs in this file is:", counter)

fasta_file_obj.close()
