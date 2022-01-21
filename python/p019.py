"""Problem 19: Counting Sundays
https://projecteuler.net/problem=19
"""
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

from helpers import solution


def solution_19(start_year, end_year, start_day=2):
    """Tracks the day of the year by adding the number of days per month.
    Counts how many times an addition is congruent to 0 mod 7.
    """
    days_per_month = dict(
        zip(range(1, 13), [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    )

    # We consider the week to start on Sunday, and 1 Jan 1901 was a Tuesday,
    # hence start_day=2
    day = start_day
    count = 0
    for year in range(start_year, end_year + 1):
        is_leap_year = year % 4 == 0 and year % 400 != 0
        days_per_month[2] = 28 + is_leap_year

        for month in range(1, 13):
            # Check for if 1 Jan 2001 ends up being a Sunday
            is_end_of_range = year == end_year and month == 12
            day += days_per_month[month]
            day %= 7
            if day == 0 and not is_end_of_range:
                count += 1

    return count


def main():
    """Main function."""
    start_year = 1901
    end_year = 2000
    ans = solution_19(start_year, end_year)
    stmt = lambda: solution_19(start_year, end_year)
    solution.print_solution(ans)
    solution.benchmark(stmt)


if __name__ == "__main__":
    main()

# Answer: 171
# Completed on Thu, 20 Jan 2022
