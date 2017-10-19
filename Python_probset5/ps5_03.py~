#!/usr/bin/env python

# Open and read the contents of a file, "Python_05.txt"
# Uppercase each line
# Print each line to new file, "Python_05_uc.txt"

Petty_song = open("Python_05.txt", "r")
uppercase_version = open("Python_05_uc.txt", "w")

for line in Petty_song:
    line = line.rstrip()
    line = line.upper()
    uppercase_version.write(line)

Petty_song.close()
uppercase_version.close()
print("Wrote 'Python_05_uc.txt'")
