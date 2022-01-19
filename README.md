# Project Euler solutions

My solutions to Project Euler problems, completed as a way for me to both brush up on Python and learn Julia.
The same algorithm is implemented in both languages, although I take advantage of base functions that are available in Julia but not Python, like prime factorization and generation.
In those cases, note that it's possible my Python implementation could use further optimization (although the point still stands that Julia is consistently faster).

Benchmarking is done with `timeit` in Python and `BenchmarkTools` in Julia.

| ID    | Description / Title                   | Date Solved   | Python Time   | Julia Time    |
|----   |----------------------------           |-------------  |-------------  |------------   |
| 1     | Multiples of 3 or 5                   | 3 Jan 2022    | 64.832 μs     | 3.064 μs      |
| 2     | Even Fibonacci numbers                | 3 Jan 2022    | 2.843 μs      | 19.177 ns     |
| 3     | Largest prime factor                  | 4 Jan 2022    | 20.146 ms     | 3.801 μs      |
| 4     | Largest palindrome product            | 4 Jan 2022    | 32.001 ms     | 4.328 ms      |
| 5     | Smallest multiple                     | 5 Jan 2022    | 25.022 µs     | 462.259 ns    |
| 6     | Sum square difference                 | 6 Jan 2022    | 22.202 µs     | 1.328 ns      |
| 7     | 10001st prime                         | 6 Jan 2022    | 46.865 ms     | 7.188 ms      |
| 8     | Largest product in a series           | 6 Jan 2022    | 1.255 ms      | 31.756 μs     |
| 9     | Special Pythagorean triplet           | 6 Jan 2022    | 174.904 µs    | 215.988 ns    |
| 10    | Summation of primes                   | 7 Jan 2022    | 1.080 s       | 4.502 ms      |
| 11    | Largest product in a grid             | 16 Jan 2022   |               |               |
| 12    | Highly divisble triangular number     | 7 Jan 2022    |               |               |
| 13    | Large sum                             | 10 Jan 2022   |               |               |
| 14    | Longest Collatz sequence              | 8 Jan 2022    |               |               |
| 15    | Lattice paths                         | 17 Jan 2022   |               |               |
| 16    | Power digit sum                       | 10 Jan 2022   |               |               |
| 18    | Maximum path sum I                    | 17 Jan 2022   |               |               |
| 20    | Factorial digit sum                   | 10 Jan 2022   |               |               |
| 21    | Amicable numbers                      | 11 Jan 2022   |               |               |
| 22    | Names scores                          | 11 Jan 2022   |               |               |
| 23    | Non-abundant sums                     | 12 Jan 2022   |               |               |
| 24    | Lexicographic permutations            | 12 Jan 2022   |               |               |
| 25    | 1000-digit Fibonacci number           | 9 Jan 2022    |               |               |
| 29    | Distinct powers                       | 12 Jan 2022   |               |               |
| 35    | Circular primes                       | 13 Jan 2022   |               |               |
| 67    | Maximum path sum II                   | 17 Jan 2022   |               |               |
