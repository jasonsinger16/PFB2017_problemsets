#!/usr/bin/env python

# Practice using pop() and remove() in combination with lists
# Print list
# Store the value returned by pop()
# Print 'popped' value and the list
# Note what has happened to the orig list

nums = [101,2,15,22,95,33,2,27,72,15,52]

print ("orig list:", nums)
print ("items included:", len(nums))
ppd_value = nums.pop()
print ("'popped' value:", ppd_value)
print ("post-'pop' list (same name!):", nums)
print ("items included:", len(nums))
