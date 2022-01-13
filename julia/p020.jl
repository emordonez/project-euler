# Problem 20: Factorial digit sum
# https://projecteuler.net/problem=20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

let x = 0
    N = 100
    N_factorial = factorial(big(N))
    x = sum(digits(N_factorial))
    println(x)
end

# Answer: 648
# Completed on Mon, 10 Jan 2022
