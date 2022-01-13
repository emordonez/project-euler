# Problem 22: Names scores
# https://projecteuler.net/problem=22
#
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

let total_score = 0
    ALPHABET = collect('A':'Z')
    ALPHA_VALUE = Dict(zip(ALPHABET, 1:26))
    
    names = join(readlines("../_files/p022.txt"))
    names = split(names, ',')
    sort!(names)
    
    for (rank, name) in enumerate(names)
        score = 0
        str = replace(name, r"[\",]*" => "")
        for ch in str
            score += ALPHA_VALUE[ch]
        end
        score *= rank
        total_score += score
    end
    println(total_score)
end

# Answer: 871198282
# Completed on Tue, 11 Jan 2022
