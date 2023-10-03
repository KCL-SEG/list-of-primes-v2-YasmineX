"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    
    n = 5
    while n * n <= num:
        if num % n == 0 or num % (n + 2) == 0:
            return False
        n += 6
    return True
    

def primes(number_of_primes):
    list = []
    number = 2
    if number_of_primes <= 0:
        raise ValueError
    
    while len(list) < number_of_primes:
        if isPrime(number):
            list.append(number)
        number += 1
    return list
