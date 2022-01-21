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
| 11    | Largest product in a grid             | 16 Jan 2022   | 377.685 µs    | 7.699 μs      |
| 12    | Highly divisble triangular number     | 7 Jan 2022    | 2.788 s       | 9.910 ms      |
| 13    | Large sum                             | 10 Jan 2022   | 594.234 µs    | 25.351 μs     |
| 14    | Longest Collatz sequence              | 8 Jan 2022    | 1.238 s       | 12.761 ms     |
| 15    | Lattice paths                         | 17 Jan 2022   | 1.397 µs      | 188.332 ns    |
| 16    | Power digit sum                       | 10 Jan 2022   | 26.733 µs     | 2.042 μs      |
| 17    | Number letter counts                  | 20 Jan 2022   | 362.466 µs    | 157.054 μs    |
| 18    | Maximum path sum I                    | 17 Jan 2022   | 22.659 µs     | 10.077 μs     |
| 19    | Counting Sundays                      | 20 Jan 2022   | 119.351 µs    | 8.355 μs      |
| 20    | Factorial digit sum                   | 10 Jan 2022   | 18.675 µs     | 1.625 μs      |
| 21    | Amicable numbers                      | 11 Jan 2022   | 53.706 ms     | 26.575 ms     |
| 22    | Names scores                          | 11 Jan 2022   | 2.224 ms      | 3.708 ms      |
| 23    | Non-abundant sums                     | 12 Jan 2022   | 1.209s        | 812.590 ms    |
| 24    | Lexicographic permutations            | 12 Jan 2022   | 484.656 ms    | 630.473 ns    |
| 25    | 1000-digit Fibonacci number           | 9 Jan 2022    | 1.499 ms      | 17.599 ms     |
| 29    | Distinct powers                       | 12 Jan 2022   |               |               |
| 35    | Circular primes                       | 13 Jan 2022   |               |               |
| 40    | Champernowne's constant               | 18 Jan 2022   |               |               |
| 48    | Self powers                           | 18 Jan 2022   |               |               |
| 67    | Maximum path sum II                   | 17 Jan 2022   |               |               |
