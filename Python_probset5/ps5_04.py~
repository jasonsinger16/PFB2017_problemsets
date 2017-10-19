#!/usr/bin/env python

# Open and print the reverse complement of each sequence in 'Python_05.fasta'
# Print the output in fasta format including the sequence name and a note in the description that this is the reverse complement
# Print to STDOUT and capture the output into a file with a command line redirect '>'

seq = open("Python_05.fasta", "r")

for line in seq:
    if ">" in line:
        line = line.rstrip()
        print(line, "reverse-complement")
    else:
        clnR = line.rstrip()
        subAt = clnR.replace('A', 't')
        subTa = subAt.replace('T', 'a')
        subCg = subTa.replace('C', 'g')
        subGc = subCg.replace('G', 'c')
        cap_allsubd = subGc.upper()
        rev_comp = cap_allsubd[::-1]
        print(rev_comp)

seq.close()
