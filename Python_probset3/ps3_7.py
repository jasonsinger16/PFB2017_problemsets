#!/usr/bin/env python

# find the start position of an EcoRI in a sequence
# calculate the first and last nucleotides of each restriction fragment, post-digest

seq = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

py_start_of_site = seq.find("GAATTC")
dna_start_of_site = py_start_of_site + 1
dna_end_of_site = dna_start_of_site + 5

print ("EcoRI recognition site in sequence begins at nt", dna_start_of_site, "and ends at nt", dna_end_of_site, "\n")

cut_site = py_start_of_site + 1
frag1 = len(seq[:cut_site])
frag2 = len(seq) - frag1

print("Fragment 1:")
print (seq[:cut_site])
print("Fragment 1 extends from nt +1 to nt +" + str(frag1))
print("Length =", frag1)

print("\nFragment 2:")
print (seq[cut_site:])
print("Fragment 2 extends from nt +" + str(frag1 + 1) + " to nt +" + str(len(seq)))
print("Length =", frag2, "\n\n")

line_template = "{}\t{}\t{}"
label1 = "Fragment 1"
label2 = "Fragment 2"
pos1 = "+1 to +" + str(frag1)
pos2 = "+" + str(frag1 + 1) + " to +" + str(len(seq))

line_Frag1 = line_template.format(label1,pos1,frag1)
line_Frag2 = line_template.format(label2,pos2,frag2)
print(line_Frag1)
print(line_Frag2)
