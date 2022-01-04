# Problem 1: Multiples of 3 or 5
# https://projecteuler.net/problem=1

x = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        x += i

print(x)

# Answer: 233168
# Completed Mon, 3 Jan 2022