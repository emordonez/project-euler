# Problem 35: Circular primes
# https://projecteuler.net/problem=35
#
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
#
# How many circular primes are there below one million?

using Primes

function rotate(n)
    rotations = Set()
    n_digits = digits(n)

    for i in 1:length(n_digits)
        rotation_digits = vcat(n_digits[i:end], n_digits[1:(i - 1)])
        # Converts the array of digits back to a number
        rotation = sum(rotation_digits .*10 .^(0:(length(n_digits) - 1)))
        push!(rotations, rotation)
    end

    return rotations
end

let circular_count = 0
    N = 1000000
    p_list = Primes.primes(N)
    
    is_prime = falses(N)
    for p in p_list
        is_prime[p] = true
    end

    for p in p_list
        rotations = rotate(p)
        circular = true
        for rotation in rotations
            if is_prime[rotation] == false
                circular = false
                break
            end
        end
        circular_count += circular
    end
    println(circular_count)
end

# Answer: 55
# Completed on Thu, 13 Jan 2022
