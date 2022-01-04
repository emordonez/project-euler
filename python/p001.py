# Problem 1: Multiples of 3 or 5
# https://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

N = 1000
x = 0
for i in range(1, N):
    if i % 3 == 0 or i % 5 == 0:
        x += i

print(x)

# Answer: 233168
# Completed Mon, 3 Jan 2022
