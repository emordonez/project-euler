# Problem 13: Large sum
# https://projecteuler.net/problem=13
#
# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
#
#   (see "../_files/p013.txt")
#

using BenchmarkTools

# Although BigInt can handle addition of numbers this large, this addition
# algorithm is more space efficient
function solution_13(nums::Vector{String}, num_length::Int, N::Int)
    total_sum_str = ""
    carry = 0
    for i in num_length:-1:1
        digits_sum = carry
        for num in nums
            digits_sum += parse(Int, num[i])
        end
        total_sum_str *= string(mod(digits_sum, 10))
        carry = div(digits_sum, 10)
    end
    
    if carry != 0
        total_sum_str *= string(carry)
        total_sum_str = reverse(total_sum_str)
    end

    return total_sum_str[1:N]
end

nums = readlines("../_files/p013.txt")
println(solution_13(nums, 50, 10))
@btime solution_13(nums, 50, 10)

# Answer: 5537376230
# Completed on Mon, 10 Jan 2022
