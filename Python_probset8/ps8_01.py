#!/usr/bin/env python

# Take a mulit-FASTA file from user input and calculate the nucleotide composition for each sequence. 
# Use a datastructure to keep count. Print out each sequence name and its compostion in this format:
# seqName\tA_count\tT_count\tG_count\C_count

fa_filename = input("Enter name of fasta-formatted file:  ")

fa_file = open(fa_filename, "r")

toplvldict = {}
for line in fa_file:
    line = line.rstrip()
    if ">" in line:
        seqname = line
        toplvldict[seqname] = ''
    else:
        acgt = line
        toplvldict[seqname] = toplvldict[seqname] + acgt

#print(len(toplvldict))


for name in toplvldict:
#    print(len(toplvldict[name]))
    numA = toplvldict[name].count('A')
    numC = toplvldict[name].count('C')
    numG = toplvldict[name].count('G')
    numT = toplvldict[name].count('T')
#    print(numA, numG)
    ntsubdict = {}
    toplvldict[name] = ntsubdict
    ntsubdict['A'] = numA
    ntsubdict['C'] = numC
    ntsubdict['G'] = numG
    ntsubdict['T'] = numT

print("\nseqName\t\tA_count\tT_count\tG_count\tC_count")
for fa_entry in toplvldict:
    seqName = fa_entry.split()[0][1:]
    A_count = str(toplvldict[fa_entry]['A'])
    C_count = str(toplvldict[fa_entry]['C'])
    G_count = str(toplvldict[fa_entry]['G'])
    T_count = str(toplvldict[fa_entry]['T'])
    print(seqName+'\t'+A_count+'\t'+T_count+'\t'+G_count+'\t'+C_count)

#print(toplvldict)
#print(toplvldict['>c0_g1_i1 len=1163 path=[1:0-1162]']['A'])
