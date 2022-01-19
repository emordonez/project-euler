"""Problem 10: Summation of primes
https://projecteuler.net/problem=10
"""
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from helpers import primes, solution


def solution_10(n):
    """Generates primes up to 2,000,000 and sums them."""
    p_gen = primes.generate_primes()
    p = 0
    prime_sum = 0

    while p < n:
        prime_sum += p
        p = next(p_gen)

    return prime_sum


def main():
    """Main function."""
    N = 2E6
    ans = solution_10(N)
    stmt = lambda: solution_10(N)
    solution.print_solution(ans)
    solution.benchmark(stmt, number=100) # This one takes longer...


if __name__ == "__main__":
    main()

# Answer: 142913828922
# Completed on Fri, 7 Jan 2022
