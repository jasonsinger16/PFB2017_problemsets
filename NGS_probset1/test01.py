#!/usr/bin/env python3

# Write a script to:
# 1) Count the number of sequences in a FASTQ file.
# 2) Output the mean and standard deviation of sequence lengths.
# 3) Calculate the mean and standard deviation of base quality scores.

import sys
import statistics













input_fastq_filename = sys.argv[1]
fastq_file = open(input_fastq_filename, 'r')

line_list = []
for line in fastq_file:
    line_list.append(line)
lines = len(line_list)

seq_list = []
for step in range(1, lines, 4):
    seq = line_list[step]
    length = len(seq)
    seq_list.append(length)
print(seq_list)
    

