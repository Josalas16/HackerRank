# Day 5: Loops
# Problem
# Objective
# In this challenge, we're going to use loops to help us do some simple math

# Task
# Given an integer, n, print its first 10 multiples. Each multiple n x i (where 1 <= i <=10) should be printed on a new
# line in the form: n x i = result

# Input Format
# A single integer, n

# Output Format
# Print 10 lines of output; each line i (where 1 <= i <= 10) contains the result of n x i in the form:
# n x i = result

# Sample Input
# 2

# Sample Output
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
#.......
# 2 x 10 = 20

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
        print(n, 'x', i, '=', n * i)