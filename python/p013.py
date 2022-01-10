# Problem 13: Large sum
# https://projecteuler.net/problem=13
#
# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
#
#   (see "../_files/p013.txt")
#

with open('../_files/p013.txt') as f:
    nums = f.read().splitlines()

# Although Python can handle arbitrarily large numbers, this addition algorithm
# is more space efficient
N = 10
num_length = 50
total_sum_str = ""
carry = 0

for i in reversed(range(num_length)):
    digits_sum = carry
    for num in nums:
        digits_sum += int(num[i])
    total_sum_str += str(digits_sum % 10)
    carry = digits_sum // 10

if carry != 0:
    total_sum_str += str(carry)
    total_sum_str = total_sum_str[::-1]

print(total_sum_str[:N])

# Answer: 5537376230
# Completed on Mon, 10 Jan 2022
