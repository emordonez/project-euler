"""Problem 4: Largest palindrome product
https://projecteuler.net/problem=4
"""
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    """Iterates over all products of three-digit numbers."""
    N = 1000
    x = -1
    for i in range(100, N):
        for j in range(i, N):
            prod = i * j
            if prod > x and str(prod) == str(prod)[::-1]:
                x = prod

    print(x)


if __name__ == "__main__":
    main()

# Answer: 906609
# Completed on Tue, 4 Jan 2022
