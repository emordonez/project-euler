"""Problem 17: Number letter counts
https://projecteuler.net/problem=17
"""
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

def main():
    """Stores letter counts in dicts."""
    def letter_count(num):
        """Returns the number of letters when spelling out num in English."""
        count = 0
        if num < 20:
            count = SUB20[num]
        elif num < 100:
            count = TENS[num // 10] + SUB20[num % 10]
        elif num < 1000:
            rem = letter_count(num % 100)
            if rem != 0:
                rem += len("and")
            count = SUB20[num // 100] + len("hundred") + rem
        elif num == 1000:
            count = len("onethousand")

        return count


    zipped_sub20 = zip(
        range(20),
        [
            "", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
        ]
    )
    zipped_tens = zip(
        range(10),
        [
            "", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"
        ]
    )
    SUB20 = {k:len(v) for k, v in zipped_sub20}
    TENS = {k:len(v) for k, v in zipped_tens}

    N = 1000
    letter_sum = 0
    for i in range(1, N + 1):
        letter_sum += letter_count(i)

    print(letter_sum)


if __name__ == "__main__":
    main()

# Answer: 21124
# Completed on Thu, 20 Jan 2022
