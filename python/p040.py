"""Problem 40: Champernowne's constant
https://projecteuler.net/problem=40
"""
# An irrational decimal fraction is created by concatenating the positive
# integers:
#
#       0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If d_n represents the nth digit of the fractional part, find the value of the
# following expression.
#
#       d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

def main():
    """Main function."""
    def d(n):
        """Returns the nth digit of Champernowne's constant."""
        return int(champernowne[n])


    N = 1000000
    champernowne = "."
    for i in range(1, N + 1):
        champernowne += str(i)

    expression = 1
    for i in range(7):
        expression *= d(10**i)

    print(expression)


if __name__ == "__main__":
    main()

# Answer: 210
# Completed on Tue, 18 Jan 2022
