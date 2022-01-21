"""Problem 16: Power digit sum
https://projecteuler.net/problem=16
"""
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

from helpers import solution


def solution_16(n):
    """Loops through the digits of 2^n and returns the sum."""
    digits_sum = 0
    for d in str(2**n):
        digits_sum += int(d)

    return digits_sum


def main():
    """Main function."""
    N = 1000
    ans = solution_16(N)
    stmt = lambda: solution_16(N)
    solution.print_solution(ans)
    solution.benchmark(stmt)


if __name__ == "__main__":
    main()

# Answer: 1366
# Completed on Mon, 10 Jan 2022
