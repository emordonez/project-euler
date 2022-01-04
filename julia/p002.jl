# Problem 2: Even Fibonacci numbers
# https://projecteuler.net/problem=2

f1, f2 = 1, 2
x = 0
while f2 < 4E6
    if iseven(f2)
        global x += f2
    end
    global f1, f2 = f2, f1 + f2
end

println(x)

# Answer: 4613732
# Completed Mon, 3 Jan 2022