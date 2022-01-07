# Problem 10: Summation of primes
# https://projecteuler.net/problem=10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

using Primes

N = 2000000
x = sum(primes(N))

println(x)

# Answer: 142913828922
# Completed on Fri, 7 Jan 2022
