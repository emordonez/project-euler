# Problem 3: Largest prime factor
# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

using BenchmarkTools
using Primes

function solution_3(N::Int)
    return last(Primes.factor(Vector, N))
end

println(solution_3(600851475143))
@btime solution_3(600851475143)

# Answer: 6857
# Completed Tue, 4 Jan 2022
