# Problem 20: Factorial digit sum
# https://projecteuler.net/problem=20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

N = 100
N_factorial = 1
for i in range(1, N + 1):
    N_factorial *= i

digits_sum = 0
for d in str(N_factorial):
    digits_sum += int(d)

print(digits_sum)

# Answer: 648
# Completed on Mon, 10 Jan 2022
