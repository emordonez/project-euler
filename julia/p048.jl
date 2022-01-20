# Problem 48: Self powers
# https://projecteuler.net/problem=48
#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

let ans = 0
    series::BigInt = 0
    for i in 1:1000
        series += big(i)^i
    end

    d = digits(series)[1:10]
    ans = foldr((a, b) -> muladd(10, b, a), d, init=0)
    println(ans)
end

# Answer: 9110846700
# Completed on Tue, 18 Jan 2022
