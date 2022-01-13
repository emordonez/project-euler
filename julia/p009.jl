# Problem 9: Special Pythagorean triplet
# https://projecteuler.net/problem=9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which,
#
#       a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Euclid's formula generates Pythagorean triples given an arbitrary pair of
# integers m > n > 0:
#
#       a = m^2 - n^2, b = 2mn, c = m^2 + n^2
#
# With the constraint a + b + c = 1000, we can find an upper bound for m and
# iterate to find n.

let x = 0
    s = 1000
    m_max = isqrt(div(s, 2))
    for m in m_max:-1:3
        for n in 2:(m - 1)
            a = abs2(m) - abs2(n)
            b = 2 * m * n
            c = abs2(m) + abs2(n)
            if a + b + c == s
                x = a * b * c
                break
            end
        end
    end
    println(x)
end

# Answer: 31875000
# Completed on Thu, 6 Jan 2022
