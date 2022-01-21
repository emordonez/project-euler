"""Problem 24: Lexicographic permutations
https://projecteuler.net/problem=24
"""
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
#       012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

from itertools import permutations
from helpers import solution


def solution_24(n, limit):
    """Permutes the range 0..n and sorts them lexicographically."""
    digits = list(range(n + 1))
    perm = sorted(permutations(digits))

    millionth = ""
    for d in perm[limit - 1]:
        millionth += str(d)

    return millionth


def main():
    """Main function."""
    n = 9
    limit = 1000000
    ans = solution_24(n, limit)
    stmt = lambda: solution_24(n, limit)
    solution.print_solution(ans)
    solution.benchmark(stmt, number=100)


if __name__ == "__main__":
    main()

# Answer: 2783915460
# Completed on Wed, 12 Jan 2022
