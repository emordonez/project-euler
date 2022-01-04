# Problem 2: Even Fibonacci numbers
# https://projecteuler.net/problem=2
#
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

f1, f2 = 1, 2
N = 4E6
x = 0
while f2 < N
    if iseven(f2)
        global x += f2
    end
    global f1, f2 = f2, f1 + f2
end

println(x)

# Answer: 4613732
# Completed Mon, 3 Jan 2022
