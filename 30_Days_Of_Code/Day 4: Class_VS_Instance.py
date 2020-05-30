# Day 4: Class vs Instance
# Objective
# In this challenge, we're going to learn about the difference between a class and an instance, because this is an
# Object Oriented concept, it's only wnabled in certain languages.

# Task
# Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a
# parameter. The constructor must assign initialAge to age after confirming the argument passed as initialAge, the
# constructor should set age to 0 and print Age is not valid, setting age to 0.. In addition you must write the
# following instance methods:
# 1. yearPasses() should increase the age instance variable by 1.
# 2. amIOld() should perform the following conditional actions:
# - if age < 13, print You are Young..
# - if age >= 13 and age < 18, print You are a teenager..
# - Otherwise, print You are old..

# Input Format
# Input is handled for you by the stub code in the editor.
# The first line contains an integer, T (the number of test cases), and the T subsequent lines
# each contain an integer denoting the age of a Person instance.

# Constraints
# - 1 <= T <= 4
# - -5 <= age <= 30

# Sample Input
# 4
# -1
# 10
# 16
# 18

# Sample Output
# Age is not valid, setting age to 0
# You are young.
# You are young.

# You are young.
# You are a teenager

# You are a teenager.
# You are old.

# You are old.
# You are old.

class Person:
    # Add some more code to run some checks on initialAge
    def __init__(self,initialAge):

    # Do some computations in here and print out the correct statement to the console
    def amIOld(self):

    # Increment the age of the person in here
    def yearPasses(self):

t = int(input())
for i in range(0,t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0,3):
        p.yearPasses()
    p.amIOld()
    print("")
