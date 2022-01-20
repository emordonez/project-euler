# Problem 40: Champernowne's constant
# https://projecteuler.net/problem=40
#
# An irrational decimal fraction is created by concatenating the positive
# integers:
#
#       0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If d_n represents the nth digit of the fractional part, find the value of the
# following expression.
#
#       d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

let expression = 1
    # Finds the nth digit of the fractional part of the constnat 
    function d(n::Int)
        pos = 0
        i = 0
        while pos < n - length(string(n))
            i += 1
            pos += length(str(i))
        end

        return parse(Int, string(i + 1)[n - pos - 1])
    end

    for i in 0:6
        expression *= d(10^i)
    end
    println(expression)
end

# Answer: 210
# Completed on Tue, 18 Jan 2022
