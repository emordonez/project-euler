# Problem 24: Lexicographic permutations
# https://projecteuler.net/problem=24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
#       012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

using BenchmarkTools
using Combinatorics

function solution_24(N::Int, limit::Int)
    millionth = ""
    digits = collect(0:N)
    millionth_perm = Combinatorics.nthperm(digits, limit)
    
    for d in millionth_perm
        millionth *= string(d)
    end

    return millionth
end

println(solution_24(9, 1000000))
@btime solution_24(9, 1000000)

# Answer: 2783915460
# Completed on Wed, 12 Jan 2022
