#!/usr/bin/env python3

# Write a python program 'kmer_counter.py' that takes command-line parameters:
#   kmer_length
#   filename.fastq
#   num_top_kmers

# The program should do the following:
#   read in the fastq file 'filename.fastq'
#   count kmers of size 'kmer_length'
#   output a table of the 'num_top_kmers' kmers sorted by abundance, descendingly.


import sys

input_filename = sys.argv[1]
kmer_length = int(sys.argv[2])
top_kmers = int(sys.argv[3])

fastq_obj = open(input_filename, 'r')

counter = 0
reads = []
for line in fastq_obj:
    line = line.rstrip()
    seq_line = counter%4
    if seq_line == 1:
         reads.append(line)
    counter +=1

# print(reads)

kmer_binner = {}
for read in reads:
    for window_start in range((len(read)-kmer_length)+1):
        kmer = read[window_start:window_start+kmer_length]
        if kmer not in kmer_binner:
            kmer_binner[kmer] = 1
        else:
            kmer_binner[kmer] += 1

# for k in kmer_binner:
#     if kmer_binner[k] == 2:
#         print(k)

sorted_binner = sorted(kmer_binner.items(), key=lambda kmer_binner: kmer_binner[1], reverse=True)  #"lambda kmer_binner:" is like "f(x)=", where 'lambda' = 'f', 'kmer_binner' = 'x', and ':' = '='

print("\n")
for n in range(top_kmers):
    print(sorted_binner[n][0], sorted_binner[n][1])
print("\n") 

fastq_obj.close()

