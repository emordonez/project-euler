"""Problem 7: 10001st prime
https://projecteuler.net/problem=7
"""
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10,001st prime number?

def generate_primes():
    """An implementation of the Sieve of Eratosthenes to generate primes
    indefinitely. Returns a generator.
    """
    i = 2
    composites = {}

    while True:
        if i not in composites:
            yield i
            composites[i * i] = [i]
        else:
            for p in composites[i]:
                composites.setdefault(i + p, []).append(p)
            del composites[i]

        i += 1


def main():
    """Iteratively generates primes until the 10,001st prime."""
    N = 10001
    primes = generate_primes()
    p = 0
    p_count = 0

    while p_count < N:
        p = next(primes)
        p_count += 1

    print(p)


if __name__ == "__main__":
    main()

# Answer: 104743
# Completed on Thu, 6 Jan 2022
