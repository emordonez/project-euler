# Problem 25: 1000-digit Fibonacci number
# https://projecteuler.net/problem=25
#
# The Fibonacci sequence is defined by the recurrence relation:
#
#       Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
#
#       F1 = 1
#       F2 = 1
#       F3 = 2
#       F4 = 3
#       F5 = 5
#       F6 = 8
#       F7 = 13
#       F8 = 21
#       F9 = 34
#       F10 = 55
#       F11 = 89
#       F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?

from math import log10


def number_of_digits(n):
    """Returns the number of digits in an integer n."""
    return int(log10(n)) + 1


i = 2
N = 1000
f1, f2 = 1, 1
while number_of_digits(f2) < N:
    f1, f2 = f2, f1 + f2
    i += 1

print(i)

# Answer: 4782
# Completed on Sun, 9 Jan 2022
