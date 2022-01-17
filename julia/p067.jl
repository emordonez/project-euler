# Problem 67: Maximum path sum II
# https://projecteuler.net/problem=67
#
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

using DelimitedFiles

# Utilizes the same dynamic programming solution as Problem 18
function path_sum(line::Matrix, prev_line::Matrix)
    for i in 1:length(filter(!isempty, line))
        line[i] += max(prev_line[i], prev_line[i + 1])
    end

    return line
end

let maximum_total = 0
    triangle = readdlm("../_files/p067.txt")
    N = size(triangle, 1)
    for i in (N - 1):-1:1
        triangle[i:i,:] = path_sum(triangle[i:i,:], triangle[i+1:i+1,:])
    end
    maximum_total = first(triangle)
    println(maximum_total)
end

# Answer: 7273
# Completed on Mon, 17 Jan 2022
