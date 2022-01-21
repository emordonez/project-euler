# Problem 17: Number letter counts
# https://projecteuler.net/problem=17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

using BenchmarkTools

function solution_17(N::Int)
    function letter_count(n::Int)
        count = 0
        if n < 20
            count = SUB20[n]
        elseif n < 100
            count = TENS[div(n, 10)] + SUB20[mod(n, 10)]
        elseif n < 1000
            rem = letter_count(mod(n, 100))
            if rem != 0
                rem += length("and")
            end
            count = SUB20[div(n, 100)] + length("hundred") + rem
        elseif n == 1000
            count = length("onethousand")
        end
    
        return count
    end
    
    zipped_sub20 = zip(
        0:19,
        [
            "", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
        ]
    )
    zipped_tens = zip(
        0:9,
        [
            "", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"
        ]
    )
    SUB20 = Dict((k, length(v)) for (k, v) in zipped_sub20)
    TENS = Dict((k, length(v)) for (k, v) in zipped_tens)
    
    letter_sum = 0
    for i in 1:N
        letter_sum += letter_count(i)
    end

    return letter_sum
end

println(solution_17(1000))
@btime solution_17(1000)

# Answer: 21124
# Completed on Thu, 20 Jan 2022
