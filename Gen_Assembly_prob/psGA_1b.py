#!/usr/bin/env python3

fasta_file_obj = open("ecoli_6X.fasta", 'r')

contig_lengths = []
for line in fasta_file_obj:
    line = line.rstrip()
    if line.startswith(">"):
        contig_lengths.append(int(line.split()[1][4:]))

print("\nThe number of contigs in this file is:", len(contig_lengths))
print("The shortest contig in this file is:",min(contig_lengths))
print("The longest contig in this file is:",max(contig_lengths))

half_assembly = (sum(contig_lengths))/2

contig_lengths.sort()
rev_sort_contig_lengths = list(reversed(contig_lengths))

contig_sum=0
for length in rev_sort_contig_lengths:
    contig_sum += length
    if contig_sum > half_assembly:
        L50 = length
        break

print("The L50 size for this file is:",L50,"\n")

#print(rev_sort_contig_lengths)
#print('{:.0f}'.format(half_assembly))


fasta_file_obj.close()
