#!/usr/bin/env python

# Create a function to format a string of DNA so that each line is no more than 60 nt long.
# INPUT: a string of DNA with or without newlines
# RETURNS: a string of DNA with lines no more than 60 nucleoties long

import sys

def wrapseq(concatted_seq):
    seq_to_be_wrapped = concatted_seq
    wrapped_seq = ''
    for pos in range(0, len(dna), 60):
        line = seq_to_be_wrapped[pos:pos+60] + "\n"
        wrapped_seq = wrapped_seq+line
    return wrapped_seq

def concatseq(dna):
    seq_to_be_concatted = dna
    concatted_seq = ''
    for line in seq_to_be_concatted:
        line = line.rstrip()
        concatted_seq = concatted_seq + line
    return concatted_seq

input_seq_name = sys.argv[1]
seq_file_object = open(input_seq_name, 'r')
dna = seq_file_object.read()

concatted = concatseq(dna)
wrapped = wrapseq(concatted)
print(wrapped)


