# Problem 16: Power digit sum
# https://projecteuler.net/problem=16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

using BenchmarkTools

function solution_16(N::Int)
    return sum(digits(big(2)^N))
end

println(solution_16(1000))
@btime solution_16(1000)

# Answer: 1366
# Completed on Mon, 10 Jan 2022
