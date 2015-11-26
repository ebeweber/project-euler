# -*- coding: utf-8 -*-
"""
The following iterative sequence is defined for the set of positive
integers:

  n → n/2 (n is even)
  n → 3n + 1 (n is odd)

Using the rule above and starting with 13,
we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


# never recompute something twice
_sequence_lengths = {1: 1}


def next_number(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1


def sequence_length(n):
    if n in _sequence_lengths:
        return _sequence_lengths[n]

    length_for_n = 1 + sequence_length(next_number(n))
    _sequence_lengths[n] = length_for_n
    return length_for_n


if __name__ == '__main__':
    max_number = 1
    max_length = 1

    for i in range(2, 1000000):

        i_length = sequence_length(i)
        if i_length > max_length:
            max_number = i
            max_length = i_length

    print 'max number: {}, max length: {}'.format(max_number, max_length)
