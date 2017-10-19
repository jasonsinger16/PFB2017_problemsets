#!/usr/bin/env python

# Sort given list.  Iterate over sorted list.  And...
# 1) Print each element
# 2) Calculate two cumulative sums, one of all the even values and one of all the odd values
# 3) Print the two sums

nums = [101,2,15,22,95,33,2,27,72,15,52]
nums.sort()
print("Contents of sorted list:")
for no in nums:
    print(no,end=' ')
print("\n")

evens = []
odds = []

for no in nums:
    if no%2==0:
        evens.append(no)
    else:
        odds.append(no)

print("Sum of evens:", sum(evens))
print("Sum of odds:", sum(odds))
