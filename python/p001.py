"""Problem 1: Multiples of 3 or 5
https://projecteuler.net/problem=1
"""
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


from helpers import solution


def solution_1(n):
    """Iterates from 1..(n - 1) for divisibility by 3 or 5."""
    return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)


def main():
    """Main function."""
    N = 1000
    ans = solution_1(N)
    stmt = lambda: solution_1(N)
    solution.print_solution(ans)
    solution.benchmark(stmt)


if __name__ == "__main__":
    main()

# Answer: 233168
# Completed Mon, 3 Jan 2022
