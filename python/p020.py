"""Problem 20: Factorial digit sum
https://projecteuler.net/problem=20
"""
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

from helpers import solution


def solution_20(n):
    """Computes n! and loops through its digits."""
    n_factorial = 1
    for i in range(1, n + 1):
        n_factorial *= i

    digits_sum = 0
    for d in str(n_factorial):
        digits_sum += int(d)

    return digits_sum


def main():
    """Main function."""
    N = 100
    ans = solution_20(N)
    stmt = lambda: solution_20(N)
    solution.print_solution(ans)
    solution.benchmark(stmt)


if __name__ == "__main__":
    main()

# Answer: 648
# Completed on Mon, 10 Jan 2022
