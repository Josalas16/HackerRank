# Day 7: Arrays

# Problem
# Objective
# Task
# Given an Array, A, of N integers, print A's elements in reverse order as a single line of space separated numbers.

# Input Format
# The first line contains an integer, N (the size of our array).
# The second line contains N space-separated integers describing array A's elements.

# Output Format
# Print the elements of array A in reverse order as a singe line of space-separated numbers.

# Sample Input
# 4
# 1 4 3 2

# Sample Output
# 2 3 4 1

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    
    arr = list(map(int, input().rstrip().split()))
    print(" ".join(str(x) for x in arr[::-1]))