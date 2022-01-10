# -*- coding: utf-8 -*-

"""Primes

Provides a variety of methods for working with prime numbers, including:

    * Generating primes
    * Prime factorization
    * Finding divisors
"""

import itertools


def divisors(n: int) -> list:
    """Returns a sorted list of divisors of n.

        Input:  36

        Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
    """
    prime_factors = factor(n)
    prime_list = list(prime_factors.keys())
    multiplicity_list = [list(range(k + 1)) for k in prime_factors.values()]

    divisors_count = 1
    for k in prime_factors.values():
        divisors_count *= k + 1
    divisors_list = [0] * divisors_count

    i = 0
    for tup in itertools.product(*multiplicity_list):
        divisor = 1
        for j, _ in enumerate(tup):
            divisor *= prime_list[j]**tup[j]

        divisors_list[i] = divisor
        i += 1

    return sorted(divisors_list)


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


def factor(n: int) -> dict:
    """Takes an integer and decomposes it into its prime factors with
    multiplicity. Returns a dict.

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
