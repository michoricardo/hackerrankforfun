"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#od es impar
#Even es par
rango1 = range(2,5)
rango2 = range(6,20)
if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    else: 
        if n in rango1:
            print("Not Weird")
        if n in rango2: 
            print("Weird")
        if n > 20: 
            print("Not Weird")
    
