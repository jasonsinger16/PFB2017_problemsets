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
print ("stored 'popped' value:", ppd_value)
print ("post-'pop' list (same name!):", nums)
print ("items included:", len(nums))


nums2 = [101,2,15,22,95,33,2,27,72,15,52]

print ("\norig list:", nums2)
print ("items included:", len(nums2))
rmd_value = nums2.remove(95)
print ("stored 'removed' value:", rmd_value)
print ("post-'remove' list (specified val was 95):", nums2)
print ("items included:", len(nums2))

# Conclusions:
# list.pop() has a default index value, the last in the list, and it remembers (stores) the value it pops
# list.remove() targets specified list elements, not index values, has no default (you must always specify) and it doesn't store the item it removes
