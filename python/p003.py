# Problem 3: Largest prime factor
# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

from math import sqrt


n = 600851475143
x = -1

# If n is composite, then any factorization of n must have at least one factor
#   smaller than the square root of n
# Note that if n were even, we first would have to divide out all powers of 2
for i in range(3, int(sqrt(n)) + 1, 2):
    while n % i == 0:
        x = i
        n /= i

# If we cannot find any such factors, then n must be prime
if n > 2:
    x = n

print(x)

# Answer: 6857
# Completed Tue, 4 Jan 2022
