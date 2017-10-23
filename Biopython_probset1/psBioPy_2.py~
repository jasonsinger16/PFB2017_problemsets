#!/usr/bin/env python3


import Bio
from Bio import Seq
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import ProteinAlphabet

fa_file_obj = open('uniprot_sprot.fa', 'r')

id_list = []
for record in SeqIO.parse(fa_file_obj, "fasta"):
    id_list.append(record.id)
no_of_records = len(id_list)
print("The number of records in this file is: {:d}".format(no_of_records))


fa_file_obj.close()
