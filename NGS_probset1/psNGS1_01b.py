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

def calc_mean_stdev(line_list):
    no_of_lines = len(line_list)
    seq_len_list = []
    for step in range(1, no_of_lines, 4):
        length = len(line_list[step])
        seq_len_list.append(length)
    meAn = statistics.mean(seq_len_list)
    stdDev = statistics.stdev(seq_len_list)
    tot_len = sum(seq_len_list)
    len_stats = []
    len_stats.append(meAn)
    len_stats.append(stdDev)
    len_stats.append(tot_len)
    return len_stats

def calc_mean_stdev_qual(line_list):
    no_of_lines = len(line_list)
    qual_lines_concat = ''
    for step in range(3, no_of_lines, 4):
        qual_lines_concat += line_list[step]
    code_scores_list = list(qual_lines_concat)
#    addup = len(code_scores_list)
    num_score_list = []
    for code_score in code_scores_list:
        num_score = ord(code_score)-33
        num_score_list.append(num_score)
#    addup = len(num_score_list)
    meAn = statistics.mean(num_score_list)
    stdDev = statistics.stdev(num_score_list)
    qual_stats = []
    qual_stats.append(meAn)
    qual_stats.append(stdDev)
    return qual_stats

input_fastq_filename = sys.argv[1]

fastq_file = open(input_fastq_filename, 'r')
counted = seqcount(fastq_file)
print("Number of FASTQ sequences:",counted)

fastq_file = open(input_fastq_filename, 'r')
line_list = []
for line in fastq_file:
    line = line.rstrip()
    line = line.rstrip('N')
    line = line.rstrip('#')
    line_list.append(line)

gotlenstats = calc_mean_stdev(line_list)
print("Mean FASTQ sequence length:",gotlenstats[0])
print("Standard deviation of FASTQ sequence length:",gotlenstats[1])
#print("Total length of all sequences combined:",gotlenstats[2])

#fastq_file = open(input_fastq_filename, 'r')
gotqualstats = calc_mean_stdev_qual(line_list)
print("Mean base quality scores over all FASTQ sequences:",gotqualstats[0])
print("Standard deviation of base quality scores over all FASTQ sequences:",gotqualstats[1]) 
#print(gotqualstats)

fastq_file.close()
