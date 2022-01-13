# Problem 3: Largest prime factor
# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

using Primes

N = 600851475143
x = last(Primes.factor(Vector, N))
println(x)

# Answer: 6857
# Completed Tue, 4 Jan 2022
