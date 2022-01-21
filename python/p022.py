"""Problem 22: Names scores
https://projecteuler.net/problem=22
"""
# Using names.txt, a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

from helpers import solution


def solution_22(names):
    """Reads names into a list, sorts, and computes name scores."""
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    alpha_value = dict(zip(alphabet, range(1, 27)))

    total_score = 0
    for i, name in enumerate(names):
        s = name[1:-1]
        score = 0
        for ch in s:
            score += alpha_value[ch]
        score *= (i + 1)
        total_score += score

    return total_score


def main():
    """Main function."""
    with open('../_files/p022.txt') as f:
        names = f.read().split(',')
        names = sorted(names)

    ans = solution_22(names)
    stmt = lambda: solution_22(names)
    solution.print_solution(ans)
    solution.benchmark(stmt)


if __name__ == "__main__":
    main()

# Answer: 871198282
# Completed on Tue, 11 Jan 2022
