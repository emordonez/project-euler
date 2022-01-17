"""Problem 67: Maximum path sum II
https://projecteuler.net/problem=67
"""
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
#       3
#       7 4
#       2 4 6
#       8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt, a 15K text file
# containing a triangle with one-hundred rows.

# Utilizes the same dynamic programming solution as Problem 18
from p018 import path_sum


def main():
    """Dynamic programming solution."""
    with open('../_files/p067.txt') as file:
        text = file.read().splitlines()
        f = lambda x: list(map(int, x.split(' ')))
        triangle = [f(line) for line in text]

    N = len(triangle)
    for i in range(N - 2, -1, -1):
        triangle[i] = path_sum(triangle[i], triangle[i + 1])

    print(triangle[0][0])


if __name__ == "__main__":
    main()

# Answer: 7273
# Completed on Mon, 17 Jan 2022
