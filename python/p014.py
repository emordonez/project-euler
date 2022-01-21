"""Problem 14: Longest Collatz sequence
https://projecteuler.net/problem=14
"""
# The following iterative sequence is defined for the set of positive integers:
#
#       n → n/2 (n is even)
#       n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
#       13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?

from helpers import solution


def solution_14(n):
    """Computes the length of Collatz sequences with starting seeds 1..n,
    while storing the lengths of previously computed sequences.
    """
    max_length = 0
    max_seed = 0
    cache = [-1 for _ in range(n + 1)]

    for i in range(1, n):
        length = 1
        k = i

        while k != 1 and k >= i:
            length += 1
            if k % 2 == 0:
                k /= 2
            else:
                k = 3 * k + 1

        cache[i] = length + cache[int(k)]

        if cache[i] > max_length:
            max_length = cache[i]
            max_seed = i

    return max_seed


def main():
    """Main function."""
    N = 1000000
    ans = solution_14(N)
    stmt = lambda: solution_14(N)
    solution.print_solution(ans)
    solution.benchmark(stmt, number=10)


if __name__ == "__main__":
    main()

# Answer: 837799
# Completed on Sat, 8 Jan 2022
