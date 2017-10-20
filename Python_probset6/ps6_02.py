#!/usr/bin/env python

# Substitute every occurrence of "Nobody" in the file 'Python_06_nobody.txt' with "Catherine"
# Write an output file with Catherine's name ==> Catherine.txt


poem_file = open('Python_06_nobody.txt', 'r')
poem_subbed = open('Python_06_Catherine.txt', 'w')

poem_text = poem_file.read()
poem_text_subbed = poem_text.replace("Nobody","Catherine")

poem_subbed.write(poem_text_subbed)

poem_file.close()
poem_subbed.close()
print("Wrote 'Python_06_Catherine.txt'")


#print(poem_text_subbed)
