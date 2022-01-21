# Problem 6: Sum square difference
# https://projecteuler.net/problem=6

# The sum of the squares of the first ten natural numbers is
#
#       1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is
#
#       (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is
#
#       3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

using BenchmarkTools

function solution_6(N::Int)
    sum_of_squares, square_of_sum = 0, 0 
    for i in 1:N
        sum_of_squares += i^2
        square_of_sum += i
    end
    square_of_sum = square_of_sum^2
    
    return square_of_sum - sum_of_squares
end

println(solution_6(100))
@btime solution_6(100)

# Answer: 25164150
# Completed on Thu, 6 Jan 2022
