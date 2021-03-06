#!/usr/bin/env python3

# This problem is found online at:  http://fasta.bioch.virginia.edu/mol_evol/pfb_python_matrices.html

# Instructions: Your goal is to write a script that reads each of the sets of data from either the SSEARCH or BLASTP outputs 
#   and produces a table with each of the scoring matrices as row, 
#   and the percent identity, alignment length, and E()-values for columns, for the top hit from each of the searches.





import sys

def capture_line(search_results):
    line_list = [] 
    for line in search_results:
        line = line.rstrip()
        if not line.startswith("#"):
#            print(line)
            line_list=line.split('\t')
            top_line_dict = dict(zip(field_names, line_list))
            break
    return top_line_dict

input_prot_size = sys.argv[1] 
matrix_list = ['BL50', 'BP62', 'VT10', 'VT160', 'VT20', 'VT40', 'VT80']
field_names = ['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits']

print("","q_len","alen","percid","evalue", sep="\t")
#compare_matrices = {}
for matrix in matrix_list:
    results_filename = "ss_rand5-"+input_prot_size+"_v_qfo_"+matrix+".txt"
    search_results = open(results_filename, 'r')

    top_hit_results = capture_line(search_results)
#    print(top_hit_results)
#    compare_matrices[matrix]=top_hit_results

    query_seq_len = int(top_hit_results['q_end'])-int(top_hit_results['q_start'])+1
    print(matrix,query_seq_len,top_hit_results['alen'],top_hit_results['percid'],top_hit_results['evalue'], sep="\t")

    search_results.close()

#print(compare_matrices)
        
# ss_rand5-800_v_qfo_BL50.txt
