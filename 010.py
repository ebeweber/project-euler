"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def sum_of_primes(n):
    """Returns the sum of primes less than n"""
    candidates = set(range(2, n))

    for i in range(2, n):
        if i in candidates:   # i is a prime number
            # remove all multiples of i from the set
            j = 2
            while i*j < n:
                if i*j in candidates:
                    candidates.remove(i*j)
                j += 1

    return sum(candidates)


if __name__ == '__main__':
    assert sum_of_primes(10) == 17
    print sum_of_primes(2000000)
