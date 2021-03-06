"""Problem 21: Amicable numbers
https://projecteuler.net/problem=21
"""
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
# 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from math import ceil, sqrt
from helpers import solution


def sum_of_proper_divisors(n):
    """Returns the sum of proper divisors of n."""
    if n < 0:
        return ValueError("n must be positive")
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


def solution_21(n):
    """Finds all amicable numbers below n and sums them."""
    nums = [False] * (n + 1)
    amicable_nums = set()

    for i in range(1, n):
        if nums[i]:
            continue

        a = i
        b = sum_of_proper_divisors(a)
        if a != b and sum_of_proper_divisors(b) == a:
            amicable_nums.add(a)
            amicable_nums.add(b)
            nums[a] = True
            nums[b] = True

    return sum(amicable_nums)


def main():
    """Main function."""
    N = 10000
    ans = solution_21(N)
    stmt = lambda: solution_21(N)
    solution.print_solution(ans)
    solution.benchmark(stmt, number=100)


if __name__ == "__main__":
    main()

# Answer: 31626
# Completed on Tue, 11 Jan 2022
