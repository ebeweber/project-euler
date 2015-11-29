"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import operator


def get_triplet_with_sum(s):
    a = 1
    b = 2
    c = s - a - b

    while b < c:
        while a < b:

            if a**2 + b**2 == c**2:
                return a, b, c

            # increment to next combination
            a += 1
            c -= 1

        # increment _b and reset _a
        b += 1
        a = 1
        c = s - b - a


if __name__ == '__main__':
    # find the triplet for 1000 and multiple the factors together
    print reduce(
        operator.mul,
        get_triplet_with_sum(1000),
        1
    )
