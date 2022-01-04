# Problem 1: Multiples of 3 or 5
# https://projecteuler.net/problem=1

x = 0
for n in 1:999
    if mod(n, 3) == 0 || mod(n , 5) == 0
        global x += n
    end
end

println(x)

# Answer: 233168
# Completed Mon, 3 Jan 2022