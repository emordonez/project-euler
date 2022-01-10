# Problem 16: Power digit sum
# https://projecteuler.net/problem=16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

N = 1000
digits_sum = 0
for d in str(2**N):
    digits_sum += int(d)

print(digits_sum)

# Answer: 1366
# Completed on Mon, 10 Jan 2022
