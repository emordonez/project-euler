"""Problem 4: Largest palindrome product
https://projecteuler.net/problem=4
"""
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

from helpers import solution


def solution_4(n):
    """Iterates over all products of three-digit numbers."""
    x = -1
    for i in range(100, n):
        for j in range(i, n):
            prod = i * j
            if prod > x and str(prod) == str(prod)[::-1]:
                x = prod

    return x


def main():
    """Main function."""
    N = 1000
    ans = solution_4(N)
    stmt = lambda: solution_4(N)
    solution.print_solution(ans)
    solution.benchmark(stmt)


if __name__ == "__main__":
    main()

# Answer: 906609
# Completed on Tue, 4 Jan 2022
