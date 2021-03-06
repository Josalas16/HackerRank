# Task
# Given a string, S, of length N that is indexed from 0 to N - 1. print its even-indexed and odd-indexed characters as
# 2 space separated strings on a single line

# Note: () is considered to be an even index.

# Input Format
# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a String, S.

# Output Format
# For each String Sj (where 0 <= j <= T - 1) print Sj's even-indexed characters, followed by a space, followed by Sj's
# odd indexed characters

# Sample Input
# 2
# Hacker
# Rank

# Sample Output
# Hce akr
# Rn ak

# Explanation
# Test Case 0: "Hacker"
# S[0] = "H"
# S[1] = "a"
# S[2] = "c"
# S[3] = "k"
# S[4] = "e"
# S[5] = "r"
# The even indices are 0, 2 and, and the odd indices are 1,3 and 5. We then printa single line of 2 space
# separated strings; the first string contains the ordered characters from S's even indices (Hce),
# and the second string contains the ordered characters from S's odd indices (akr).
# Test Case 1: "Rank"
# S[0] = "R"
# S[1] = "a"
# S[2] = "n"
# S[3] = "k"
# The even indices are 0 and 2, and the odd indices are 1 and 3. We then print a single line of 2
# space separated strings; the first string contains the ordered characters from S's even indices (Rn),
# and the second string contains the ordered characters from S's odd indices (ak).

N = int(input())
lst = []
if(N >= 1 and N <= 10):
    for i in range(N):
        lst.append(input())
for str in lst:
    print("{} {}".format(str[::2], str[1::2]))