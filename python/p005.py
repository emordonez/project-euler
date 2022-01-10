# Problem 5: Smallest multiple
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

def factor(n):
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


# The LCM is the product of all prime factors in the range 1 to 20, with each
#   prime raised to the highest power that appears in a factorization in this
#   range
factor_maps = [factor(n) for n in range(2, 21)]
prime_counts = {p:1 for p in [2, 3, 5, 7, 11, 13, 17, 19]}

for factorization in factor_maps:
    for p, count in factorization.items():
        prime_counts[p] = max(count, prime_counts[p])

x = 1
for k, v in prime_counts.items():
    x *= k**v

print(x)

# Answer: 232792560
# Completed on Wed, 5 Jan 2022
