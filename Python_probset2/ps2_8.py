#!/usr/bin/env python

# Determines if a value
#    1) is positive or negative
#    2) if positive, is bigger or smaller than 50
#    3) if smaller than 50, is even or odd
#    4) if larger than 50, is divisible by 3.

# sys.argv[1]

import sys

num = int(sys.argv[1])

if ((abs(num) + num) > 0):
    print("number is positive")
    if num < 50:
        print("number is smaller than 50")
        if num%2 == 0:
            print("number is even")
        else:
            print("number is odd")
    elif num > 50:
        print("number is larger than 50")
        if num%3 == 0:
            print("number is divisible by 3")
        else:
            print("number is not divisible by 3")
    else:
        print("number must be 50")
elif num == 0:
    print ("number must be 0")
else:
    print("number is negative")
    if num%2 == 0:
        print("number is even")
    else:
        print("number is odd")
