"""Problem 9: Special Pythagorean triplet
https://projecteuler.net/problem=9
"""
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which,
#
#       a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt
from helpers import solution


def solution_9(s):
    """Utilizes Euclid's formula for Pythagorean triples to solve for a, b, c
    such that a + b + c = s.
    """
    # Euclid's formula generates Pythagorean triples given an arbitrary pair of
    # integers m > n > 0:
    #
    #       a = m^2 - n^2, b = 2mn, c = m^2 + n^2
    #
    # With the constraint a + b + c = 1000, we can find an upper bound for m
    # and iterate to find n.
    m_max = int(sqrt(s / 2))
    x = 0
    for m in range(m_max, 2, -1):
        for n in range(2, m):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if a + b + c == s:
                x = a * b * c
                break

    return x


def main():
    """Main function."""
    s = 1000
    ans = solution_9(s)
    stmt = lambda: solution_9(s)
    solution.print_solution(ans)
    solution.benchmark(stmt)


if __name__ == "__main__":
    main()

# Answer: 31875000
# Completed on Thu, 6 Jan 2022
