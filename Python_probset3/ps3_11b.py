#!/usr/bin/env python

# Interogate the difference between two ways to copy a list. Both are not correct.  11a is the first way. This (11b) is the second way.  

list = ['a', 'bb', 'ccc']
list_copy = list.copy()

print("list:", list)
print("list_copy:", list_copy, "\n")

list_copy.append('dddd')

print("After appending to list_copy, here is orig 'list' variable, again:", list)
print("After appending to list_copy, here is 'list_copy' variable, again:", list_copy)


# After looking at results, this is the RIGHT way to copy a list.   :)
