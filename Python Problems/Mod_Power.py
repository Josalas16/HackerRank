# Power - Mod Power

# Problem
# So far, we have only heard of Python's powers. Now, we will witness them!
# Powers or exponents in Python can be calculated using the built-in power function.
# Call the power function a^b as shown below
# >>> pow(a,b) or a**b

# It's also possible to calculate a^b mod m
# pow(a,b,m)

# This is very helpful in computations where you have to print the resultant & mod.
# Note: Here, a and b can be floats or negatives, but, if a third argument is present, b cannot be aggressive.

# Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. Frankly speaking,
# we will never use math.pow().

# Task
# You are given three integers: a, b, and m, respectively. Print two lines.
# The first line should print the result of pow(a, b). The second line should print the result of pow(a, b, m).

# Input Format
# The first line contains a, the second line contains b, and the third line contains m.

# Sample Input
# 3
# 4
# 5

# Sample Output
# 81
# 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))
print(pow(a,b,m))

