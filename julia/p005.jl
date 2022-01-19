# Problem 5: Smallest multiple
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

using BenchmarkTools

function solution_5(N::Int)
    return lcm(collect(1:N))
end

println(solution_5(20))
@btime solution_5(20)

# Answer: 232792560
# Completed on Wed, 5 Jan 2022
