#!/usr/bin/env python3

# Create an object of class type 'Ontology' with the gene ontology owl file.
# Get the term name for a specific Gene ontology accession (i.e., GO:0006355) from the command line
# Use 'pronto rchildren()' to retrieve all children terms of your term and to store the ID of each term in a dictionary with the term name as the value
# [use the 'id' method to retrieve the id of each term object that is returned by 'rchildren()']
# Also add the parent term to the dictionary

# Open a file generated from biomart with these columns:
#    Gene or transcript ID
#    GO TERM ID
#    GO TERM Name
# Check to see if each gene's GO TERM is the provided parent GO TERM ID or one of its children.    


import pronto
import sys

GO_term = sys.argv[1]

ont = pronto.Ontology('/Users/admin/go.owl')
term_obj = ont[GO_term]
term_name = term_obj.name
print("These genes have all been annotated with" , GO_term + ', "' + term_name + '" or any of its child terms' )


all_children = {}
for child in ont[GO_term].rchildren():
    all_children[child.id] = child.name
all_children[GO_term] = term_name

print(len(all_children))
