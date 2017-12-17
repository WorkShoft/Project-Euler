"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import unittest, math

NUMBER = 600851475143
smallPrimes = [2, 3, 5, 7]


def factors(number):
    """
    Number of factors < sqrt(number)
    """
    
    for n in range(1, int(math.sqrt(number) + 1)):
        if number % n == 0:
            yield n    
    
def primes(factors):
    for f in factors:
        if is_prime(f):
            yield f

def is_prime(number):
    if n_factors(number) == 1:
        return True
    else:
        return False
            
#Kamil Kisiel
def count_iterable(i):
    return sum(1 for e in i)

def n_factors(number):
    return count_iterable(factors(number))

def n_prime_factors(number):
    unique_factors = set()
    for n in factors(number):
        if n != 1 & is_prime(n):
            unique_factors.add(n)

    return len(unique_factors)

def largest_number(sequence):
    return max(sequence)

def largest_prime_factor(number):
    return largest_number(primes(factors(number)))

class TestFactors(unittest.TestCase):
    def test_number_of_prime_factors_smaller_than_sqrt(self):
        self.assertEqual(n_prime_factors(9), 1)
        self.assertEqual(n_prime_factors(87), 1)


print(largest_prime_factor(NUMBER))
