# Problem 20: Factorial digit sum
# https://projecteuler.net/problem=20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

using BenchmarkTools

function solution_20(n::Int)
    n_factorial = factorial(big(n))

    return sum(digits(n_factorial))
end

println(solution_20(100))
@btime solution_20(100)

# Answer: 648
# Completed on Mon, 10 Jan 2022
