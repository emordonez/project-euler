# Problem 19: Counting Sundays
# https://projecteuler.net/problem=19
#
# You are given the following information, but you may prefer to do some
# research for yourself.
#
#       1 Jan 1900 was a Monday.
#
#       Thirty days has September,
#       April, June and November.
#       All the rest have thirty-one,
#       Saving February alone,
#       Which has twenty-eight, rain or shine.
#       And on leap years, twenty-nine.
#
#       A leap year occurs on any year evenly divisible by 4, but not on a
#       century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

using BenchmarkTools

function solution_19(start_year::Int, end_year::Int, start_day::Int=2)
    days_per_month = Dict(
        zip(1:12, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    )
    
    # We consider the week to start on Sunday, and 1 Jan 1901 was a Tuesday,
    # hence start_day=2
    day = start_day
    count = 0
    for year in start_year:end_year
        is_leap_year = mod(year, 4) == 0 && mod(year, 400) != 0
        days_per_month[2] = 28 + is_leap_year
        
        for month in 1:12
            # Check for if 1 Jan 2001 ends up being a Sunday
            is_end_of_range = year == end_year && month == 12
            day += days_per_month[month]
            day = mod(day, 7)
            if day == 0 && !is_end_of_range
                count += 1
            end
        end
    end            
    
    return count
end

println(solution_19(1901, 2000))
@btime solution_19(1901, 2000)

# Answer: 171
# Completed on Thu, 20 Jan 2022
