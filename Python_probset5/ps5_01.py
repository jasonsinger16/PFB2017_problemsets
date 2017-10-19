#!/usr/bin/env python

# Open and read the contents of a file, Python_05.txt
# Uppercase each line
# Print each line to STDOUT

Petty_song = open("Python_05.txt", "r")
for line in Petty_song:
    line = line.rstrip()
    line = line.upper()
    print(line)
print("\n")
Petty_song.close()
