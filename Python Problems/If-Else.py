# Python If-Else

# Task
# Given an integer, n, perform the following conditional actions:
# 1. If n is odd, print Weird
# 2. If n is even and in the inclusive range of 2 to 5, print Not Weird
# 3. If n is even and in the inclusive range pf 6 to 20, print Weird
# 4. If n is even and greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n

# Constraints
# 1 <= n <= 100

# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    if (n % 2) != 0:
        print("Weird")
    elif (n % 2) == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif (n % 2) and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
