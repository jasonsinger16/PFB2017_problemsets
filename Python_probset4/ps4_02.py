#!/usr/bin/env python

# A script that uses a while loop to calculate the factorial of 1000

from decimal import Decimal
counter = 1
factorial_exp = '1'

while counter < 1000:
    counter += 1
    factorial_exp += ("*"+str(counter))
print(factorial_exp)
answer = (eval(factorial_exp))
print(answer)
print('{:.2e}'.format(answer))
