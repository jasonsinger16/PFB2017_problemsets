#!/usr/bin/env python

# Open and print the reverse complement of each sequence in 'Python_05_v2.fasta'
# Print the output in fasta format including the sequence name and a note in the description that this is the reverse complement
# Print to STDOUT and capture the output into a file with a command line redirect '>'

seqs_file = open("Python_05_v2.fasta", "r")
concat_seqs = {}

for line in seqs_file:
    line = line.rstrip()
    if ">" in line:
        hdr = line
        concat_seqs[hdr]=''
    else:
        seq = line
        concat_seqs[hdr]=concat_seqs[hdr]+seq

for khdr in concat_seqs:    
    proc_seq = concat_seqs[khdr]
    subAt = proc_seq.replace('A', 't')
    subTa = subAt.replace('T', 'a')
    subCg = subTa.replace('C', 'g')
    subGc = subCg.replace('G', 'c')
    cap_allsubd = subGc.upper()
    rev_comp = cap_allsubd[::-1]
    concat_seqs[khdr] = rev_comp

for k2hdr in concat_seqs:
    print(k2hdr + ", reverse-complement")
    long_seq = concat_seqs[k2hdr]
    linelength = 96
    linelist = []
    for pos in range(0, len(long_seq), linelength):
        linelist = linelist + [long_seq[pos:pos+linelength]]
    for newline in linelist:
        print(newline)

seqs_file.close()
