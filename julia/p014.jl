# Problem 14: Longest Collatz sequence
# https://projecteuler.net/problem=14
#
# The following iterative sequence is defined for the set of positive integers:
#
#       n → n/2 (n is even)
#       n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
#       13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?

using BenchmarkTools

function solution_14(N::Int)
    max_length = 0
    max_seed = 0
    cache = Array{Int64}(undef, N - 1)
    fill!(cache, -1)

    for i in 1:(N - 1)
        length = 1
        n = i

        while n != 1 && n >= i
            length += 1
            if iseven(n)
                n = div(n, 2)
            else
                n = 3 * n + 1
            end
        end

        cache[i] = length + cache[n]
        if cache[i] > max_length
            max_length = cache[i]
            max_seed = i
        end
    end
    
    return max_seed
end

println(solution_14(1000000))
@btime solution_14(1000000)

# Answer: 837799
# Completed on Sat, 8 Jan 2022
