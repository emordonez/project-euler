"""Problem 6: Sum square difference
https://projecteuler.net/problem=6
"""
# The sum of the squares of the first ten natural numbers is
#
#       1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is
#
#       (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is
#
#       3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

from helpers import solution


def solution_6(n):
    """Iterates 1..n to find the sum of squares and square of the sum."""
    sum_of_squares = 0
    square_of_sum = 0

    for i in range(1, n + 1):
        sum_of_squares += i**2
        square_of_sum += i
    square_of_sum *= square_of_sum

    return square_of_sum - sum_of_squares


def main():
    """Main function."""
    N = 100
    ans = solution_6(N)
    stmt = lambda: solution_6(N)
    solution.print_solution(ans)
    solution.benchmark(stmt)


if __name__ == "__main__":
    main()

# Answer: 25164150
# Completed on Thu, 6 Jan 2022
