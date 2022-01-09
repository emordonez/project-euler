# Problem 1: Multiples of 3 or 5
# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

let x = 0
    N = 1000
    for i in 1:(N - 1)
        if mod(i, 3) == 0 || mod(i , 5) == 0
            x += i
        end
    end
    println(x)
end

# Answer: 233168
# Completed Mon, 3 Jan 2022
