# -*- coding: utf-8 -*-
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import math


def factorial_sum(n):
    return sum([int(d) for d in str(math.factorial(n))])


if __name__ == '__main__':
    assert factorial_sum(10) == 27
    print factorial_sum(100)
