"""Problem 48: Self powers
https://projecteuler.net/problem=48
"""
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def main():
    """Sums the series and slices the last ten digits as a string."""
    n = 1000
    k = 10
    series = 0
    for i in range(1, n + 1):
        series += i**i
    print(str(series)[-k:])


if __name__ == "__main__":
    main()

# Answer: 9110846700
# Completed on Tue, 18 Jan 2022
