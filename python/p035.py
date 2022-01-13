"""Problem 35: Circular primes
https://projecteuler.net/problem=35
"""
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
#
# How many circular primes are there below one million?

from helpers import primes


def rotate(n):
    """Returns the set of rotated digits of n.

        Input:  197

        Output: {197, 971, 719}
    """
    n_str = str(n)

    return {int(n_str[i:] + n_str[:i]) for i in range(len(n_str))}


def main():
    """Generates all primes below 1,000,000 into a list, then loops and rotates
    digits to see if the rotation is one of the stored primes.
    """
    p_gen = primes.generate_primes()
    p_list = []
    p = next(p_gen)

    N = 1000000
    is_prime = [False] * N

    while p < N:
        p_list.append(p)
        is_prime[p] = True
        p = next(p_gen)

    circular_count = 0
    for p in p_list:
        rotations = rotate(p)
        circular = True
        for rotation in rotations:
            if not is_prime[rotation]:
                circular = False
                break
        circular_count += int(circular)

    print(circular_count)


if __name__ == "__main__":
    main()

# Answer: 55
# Completed on Thu, 13 Jan 2022
