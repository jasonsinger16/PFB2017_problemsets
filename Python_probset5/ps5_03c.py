#!/usr/bin/env python

# Open and print the reverse complement of each sequence in 'Python_05_v2.fasta'
# Print the output in fasta format including the sequence name and a note in the description that this is the reverse complement
# Print to STDOUT and capture the output into a file with a command line redirect '>'

seqs_file = open("Python_05_v2.fasta", "r")
concat_seqs = {}

for line in seqs_file:                          # convert wrapped fasta-format file into dictionary
    line = line.rstrip()
    if ">" in line:
        hdr = line
        concat_seqs[hdr]=''                     # set header as key
    else:
        seq = line
        concat_seqs[hdr]=concat_seqs[hdr]+seq   # concatenate originally wrapped lines of sequence into a single string = value in key:value pair

for khdr in concat_seqs:
    proc_seq = concat_seqs[khdr]                # replace values(sequences) in dictionary with the reverse-complement of the same seq
    subAt = proc_seq.replace('A', 't')
    subTa = subAt.replace('T', 'a')
    subCg = subTa.replace('C', 'g')
    subGc = subCg.replace('G', 'c')
    cap_allsubd = subGc.upper()
    rev_comp = cap_allsubd[::-1]
    concat_seqs[khdr] = rev_comp

for k2hdr in concat_seqs:                      # iterate over dictionary
    print(k2hdr + ", reverse-complement")      # modify header line to denote that reverse-comp is now displayed, instead of orig seq
    long_seq = concat_seqs[k2hdr]
    linelength = 96
    linelist = []                              # split rev-comp sequences into 96char chuncks and print out new fasta file
    for pos in range(0, len(long_seq), linelength):
        linelist = linelist + [long_seq[pos:pos+linelength]]   ### here, putting chunks of sequence into a list and then printing out list  
    for newline in linelist:                                   ### but found out later that I'm adding one unnecessary step
        print(newline)                                         ### could just break (slice) chunks off the string and print them
                                                               ### didn't need to create the list
seqs_file.close()
