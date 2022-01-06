# Problem 7: 10001st prime
# https://projecteuler.net/problem=7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10,001st prime number?

using Primes

n = 10001
x = prime(n)

println(x)

# Answer: 104743
# Completed on Thu, 6 Jan 2022
