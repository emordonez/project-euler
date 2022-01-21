# Problem 23: Non-abundant sums
# https://projecteuler.net/problem=23
#
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

using BenchmarkTools

function d(n::Int)
    if n <= 1
        return 0
    end

    s = 1
    sqrt_n = ceil(sqrt(n))
    for i in 2:(sqrt_n - 1)
        if mod(n, i) == 0
            s += i + div(n, i)
        end
    end

    return s + (sqrt_n^2 == n ? sqrt_n : 0)
end

function solution_23(N::Int)
    abundants = [i for i in 1:N if d(i) > i]
    abundant_sums = unique((abundants .+ abundants'))
    
    return sum(setdiff(1:N, abundant_sums))
end

println(solution_23(28123))
@btime solution_23(28123)

# Answer: 4179871
# Completed on Wed, 12 Jan 2022
