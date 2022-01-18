# -*- coding: utf-8 -*-

"""Solution

Provides helper functions to pretty print and benchmark problem solutions,
using timeit.
"""

import math
import timeit
from typing import Callable


def benchmark(stmt: Callable, repeat=5, number=1000) -> None:
    """Benchmarks the solution using timeit."""
    def to_si(d: float, sep=' '):
        """Converts a number to a string with an SI prefix. See here for source:
        https://shorturl.at/aqrIK
        """
        inc_prefixes = ['k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
        dec_prefixes = ['m', 'µ', 'n', 'p', 'f', 'a', 'z', 'y']

        if d == 0:
            return str(0)

        degree = int(math.floor(math.log10(math.fabs(d)) / 3))
        prefix = ''

        if degree != 0:
            ds = degree / math.fabs(degree)
            if ds == 1:
                if degree - 1 < len(inc_prefixes):
                    prefix = inc_prefixes[degree - 1]
                else:
                    prefix = dec_prefixes[-1]
                    degree = len(inc_prefixes)
            elif ds == -1:
                if -degree - 1 < len(dec_prefixes):
                    prefix = dec_prefixes[-degree - 1]
                else:
                    prefix = dec_prefixes[-1]
                    degree = -len(dec_prefixes)

            scaled = float(d * math.pow(1000, -degree))
            s = "{scaled:.3f}{sep}{prefix}".format(scaled=scaled,
                                                    sep=sep,
                                                    prefix=prefix)
        else:
            s = "{d}".format(d=d)

        return s


    t = min(timeit.repeat(stmt=stmt, repeat=repeat, number=number)) / number
    print("Best of {total} loops: {time}s".format(
        total = repeat * number,
        time = to_si(t)
        )
    )


def print_solution(ans) -> None:
    """Prints the answer."""
    print("Answer: {}".format(ans))
