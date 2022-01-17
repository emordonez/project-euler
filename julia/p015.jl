# Problem 15: Lattice paths
# https://projecteuler.net/problem=15
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

let num_paths = 0
    N = 21
    num_paths = binomial(2 * (N - 1), N - 1)
    println(num_paths)
end

# Answer: 137846528820
# Completed on Mon, 17 Jan 2022
