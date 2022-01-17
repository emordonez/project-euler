"""Problem 15: Lattice paths
https://projecteuler.net/problem=15
"""
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

from math import comb


def main():
    """For a square array of N x N points and only able to move to the right
    and down, the number of routes from the top left to bottom right corner is
    given by 2 * (N - 1) choose (N - 1).
    """

    # There are 20 squares in the grid but 21 points
    N = 21
    num_paths = comb(2 * (N - 1), N - 1)

    print(num_paths)


if __name__ == "__main__":
    main()

# Answer: 137846528820
# Completed on Mon, 17 Jan 2022
