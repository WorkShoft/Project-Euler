import math, unittest
from functools import reduce


def factor(number):
    for i in range(2, number + 1):
        if number % i == 0:
            yield i

#agf
def prime_factors(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    factors = []
    while n > 1:
        for prime in primes:
            if n % prime == 0:
                n /= prime
                factors.append(prime)


    return factors


def prime_factors_sequence(sequence):
    factors = []
    for number in sequence:
        factors.append(prime_factors(number))
    return factors


def lcm(sequence):

    base_power = {i: 0 for i in range(2, 20)}

    unique_factors = []
    
    for s in sequence:
        for n in s:
            if n not in unique_factors:
                unique_factors.append(n)

    
    for f in unique_factors:
        for s in sequence:
            if s.count(f) > base_power[f]:
                    base_power[f] = s.count(f)

    solution = 1

    
    for k,v in base_power.items():
        solution *= k**v

    return solution

       

solution = lcm(prime_factors_sequence(range(2, 20)))
print(solution)
#print(prime_factors_sequence(range(2, 20)))
