# Problem 21: Amicable numbers
# https://projecteuler.net/problem=21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
# 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

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

function solution_21(N::Int)
    amicable_nums = Set{Int}()
    nums = Array{Bool}(undef, N - 1)

    for i in 1:(N - 1)
        if nums[i] == true
            continue
        end

        a::Int = i
        b::Int = d(a)
        if a != b && d(b) == a
            push!(amicable_nums, a, b)
            nums[a] = true
            nums[b] = true
        end
    end

    return sum(amicable_nums)
end

println(solution_21(10000))
@btime solution_21(10000)

# Answer: 31626
# Completed on Tue, 11 Jan 2022
