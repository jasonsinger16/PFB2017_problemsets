#!/usr/bin/env python3

# Write a script to:
# 1) Count the number of sequences in a FASTQ file.
# 2) Output the mean and standard deviation of sequence lengths.
# 3) Calculate the mean and standard deviation of base quality scores.

import sys
import statistics

def seqcount(file):
    read_counter = 0
    for line in file:
        if ":" in line:
            read_counter += 1
    seqlines = read_counter
    return seqlines

def calc_mean_stdev(file):

    line_list = []
    for line in file:
        line = line.rstrip()
        line = line.rstrip('N')
        line_list.append(line)
    lines = len(line_list)

#    seq_list = []
    seq_len_list = []
    for step in range(1, lines, 4):
        length = len(line_list[step])
#        seq_list.append(line_list[step])
        seq_len_list.append(length)
    meAn = statistics.mean(seq_len_list)
    stdDev = statistics.stdev(seq_len_list)
    len_stats = []
    len_stats.append(meAn)
    len_stats.append(stdDev)
    return len_stats


input_fastq_filename = sys.argv[1]

fastq_file = open(input_fastq_filename, 'r')
counted = seqcount(fastq_file)
print("Number of FASTQ sequences:",counted)

fastq_file = open(input_fastq_filename, 'r')
gotlenstats = calc_mean_stdev(fastq_file)
print("Mean FASTQ sequence length:",gotlenstats[0])
print("Standard deviation of FASTQ sequence length:",gotlenstats[1])

fastq_file = open(input_fastq_filename, 'r')


fastq_file.close()
