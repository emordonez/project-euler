# Problem 10: Summation of primes
# https://projecteuler.net/problem=10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from helpers import primes

N = 2E6
p = 0
p_gen = primes.generate_primes()
prime_sum = 0

while p < N:
    prime_sum += p
    p = next(p_gen)

print(prime_sum)

# Answer: 142913828922
# Completed on Fri, 7 Jan 2022
