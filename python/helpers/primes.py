# -*- coding: utf-8 -*-

"""Primes

Provides a variety of methods for working with prime numbers, including:

    * Generating primes
    * Prime factorization
"""
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


def prime_factorization(n):
    """Takes an integer and decomposes it into its prime factors.
    Returns a dict.

    Input:  120
    Output: {2: 3, 3: 1, 5: 1}
    """
    i = 2
    factors = []
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n /= i
        else:
            i += 1

    return {p:factors.count(p) for p in factors}
