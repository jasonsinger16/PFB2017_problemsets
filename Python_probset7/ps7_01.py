#!/usr/bin/env python

# Create a function to format a string of DNA so that each line is no more than 60 nt long.
# INPUT: a string of DNA without newlines
# RETURNS: a string of DNA with lines no more than 60 nucleoties long

import sys

def wrapseq(dna):
    seq_to_be_wrapped = dna
    wrapped_seq = ''
    for pos in range(0, len(dna), 60):
        line = seq_to_be_wrapped[pos:pos+60] + "\n"
        wrapped_seq = wrapped_seq+line
    return wrapped_seq

input_seq_name = sys.argv[1]
seq_file_object = open(input_seq_name, 'r')
dna = seq_file_object.read()

print(wrapseq(dna))


