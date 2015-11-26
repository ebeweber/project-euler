"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


def highest_prime_factor(n):
    """Returns the largest prime factor of the int n.

    Uses the Sieve of Erathosthenes to generate all prime
    numbers < n and then selects the highest candidate that
    goes into n.
    """
    max_candidate = int(math.sqrt(n))
    candidates = set(range(2, max_candidate))

    for i in range(2, max_candidate):
        if i in candidates:   # i is a prime number
            # remove all multiples of i from the set
            j = 2
            while i*j < max_candidate:
                if i*j in candidates:
                    candidates.remove(i*j)
                j += 1

            # remove i if it is not a factor
            if n % i != 0:
                candidates.remove(i)

    return max(candidates)


print highest_prime_factor(600851475143)
