#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  #the fix to the code
    return result

f = factorial(int(sys.argv[1]))
print(f)
