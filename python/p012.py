# Problem 12: Highly divisble triangular number
# https://projecteuler.net/problem=12
#
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
# ten terms would be:
#
#       1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#       1: 1
#       3: 1,3
#       6: 1,2,3,6
#      10: 1,2,5,10
#      15: 1,3,5,15
#      21: 1,3,7,21
#      28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred
# divisors?

from helpers import primes


triangle = 0
i = 1
N = 500
max_divisors = 0

# Given a natural number n and its prime factorization n = p^a p^b ... p^k, the
# number of divisors of n is given by (a + 1)(b +1)...(k + 1)
while max_divisors <= N:
    divisors = 1
    triangle += i
    for k in primes.prime_factorization(triangle).values():
        divisors *= k + 1

    max_divisors = max(divisors, max_divisors)
    i += 1

print(triangle)

# Answer: 76576500
# Completed on Thu, 7 Jan 2022