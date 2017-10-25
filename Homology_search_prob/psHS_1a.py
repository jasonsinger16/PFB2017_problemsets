#!/usr/bin/env python3

import sys
import re

def capture_line(search_results):
    line_list = [] 
    for line in search_results:
        line = line.rstrip()
    #    comment_line = re.compile("^#")
        if "#" not in line:
#            print(line)
            line_list=line.split('\t')
            top_line_dict = dict(zip(field_names, line_list))
            break
    return top_line_dict

input_prot_size = sys.argv[1] 
matrix_list = ['BL50', 'BP62', 'VT10', 'VT160', 'VT20', 'VT40', 'VT80']
field_names = ['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits']

print("\talen\tpercid\tevalue")
#compare_matrices = {}
for matrix in matrix_list:
    results_filename = "ss_rand5-"+input_prot_size+"_v_qfo_"+matrix+".txt"
    search_results = open(results_filename, 'r')

    top_hit_results = capture_line(search_results)
#    print(top_hit_results)
#    compare_matrices[matrix]=top_hit_results

    print(matrix+"\t"+top_hit_results['alen']+"\t"+top_hit_results['percid']+"\t"+top_hit_results['evalue'])

    search_results.close()

#print(compare_matrices)
        
# ss_rand5-800_v_qfo_BL50.txt
