"""Problem 23: Non-abundant sums
https://projecteuler.net/problem=23
"""
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

from itertools import compress
from math import ceil, sqrt


def sum_of_proper_divisors(n):
    """Returns the sum of proper divisors of n."""
    if n < 0:
        raise ValueError("n must be positive")
    elif n == 0:
        return
    elif n == 1:
        return 0

    s = 1
    sqrt_n = ceil(sqrt(n))
    for i in range(2, sqrt_n):
        if n % i == 0:
            s += i + n // i

    return s + (sqrt_n if sqrt_n ** 2 == n else 0)


def main():
    """Finds all abundant numbers less than 28,123, then keeps track of
    abundant sums in a bit mask."""
    N = 28123
    abundants = [i for i in range(12, N + 1) if sum_of_proper_divisors(i) > i]
    abundant_sums = [True] * (N + 1)

    for i, a in enumerate(abundants):
        for b in abundants[i:]:
            if a + b > N:
                break
            abundant_sums[a + b - 1] = False
    non_abundant_sum = sum(compress(range(1, N + 1), abundant_sums))
    print(non_abundant_sum)


if __name__ == "__main__":
    main()

# Answer: 4179871
# Completed on Wed, 12 Jan 2022
