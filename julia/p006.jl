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

x = 0
let sum_of_squares = 0, square_of_sum = 0
    for i in 1:100
        sum_of_squares += abs2(i)
        square_of_sum += i
    end
    square_of_sum = abs2(square_of_sum)
    global x = square_of_sum - sum_of_squares
end

println(x)

# Answer: 25164150
# Completed on Thu, 6 Jan 2022
