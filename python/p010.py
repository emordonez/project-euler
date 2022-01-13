"""Problem 10: Summation of primes
https://projecteuler.net/problem=10
"""
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from helpers import primes


def main():
    """Generates primes up to 2,000,000 and sums them."""
    N = 2E6
    p_gen = primes.generate_primes()
    p = 0
    prime_sum = 0

    while p < N:
        prime_sum += p
        p = next(p_gen)

    print(prime_sum)


if __name__ == "__main__":
    main()

# Answer: 142913828922
# Completed on Fri, 7 Jan 2022
