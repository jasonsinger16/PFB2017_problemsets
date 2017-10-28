#!/usr/bin/env python3

# Make a list of all the descriptions (the full header lines) in a given FASTA file.
# Extract just the genus and species from each description.
# Count the number of sequences present for that genus/species combination.

import re
import Bio
from Bio import Seq
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import ProteinAlphabet

# for the particular type of fasta file being used in this problem, the fields stored in the SeqIO SeqRecord are:
# 1) ID
# 2) Name
# 3) Description
# 4) Number of features
# 5) Seq('actual protein sequence', the alphabet used())

fa_file_obj = open('uniprot_testset.fa', 'r')

descript_list = []
for record in SeqIO.parse(fa_file_obj, "fasta"):
    descript_list.append(record.description)
no_of_records = len(descript_list)
print("The number of records in this file is: {:d}".format(no_of_records))
# print(descript_list)

regex_capture_list = []
gen_spec_regex = re.compile("OS=[A-Z][a-z]+ [a-z]+ v?i?r?u?s?|OS=[A-Z][a-z]+ [a-z]+ [a-z]+ v?i?r?u?s?")
for descript in descript_list:
    hit = re.search(gen_spec_regex, descript)
    if hit:
        regex_capture_list.append(hit)
for match_obj in regex_capture_list:
    print(match_obj.string)
print(regex_capture_list)
print(len(regex_capture_list))
print(regex_capture_list[0])

fa_file_obj.close()
