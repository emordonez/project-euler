# Problem 10: Summation of primes
# https://projecteuler.net/problem=10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

using BenchmarkTools
using Primes

function solution_10(N::Int)
    return sum(primes(N))
end

println(solution_10(2000000))
@btime solution_10(2000000)

# Answer: 142913828922
# Completed on Fri, 7 Jan 2022
