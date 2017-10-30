import math

__author__ = 'erlafont'

if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")


def is_prime(number):
    for index in range(2,math.ceil(math.sqrt(number))+1):
        if number % index == 0 and number != index:
            return False
    return True


def find_all_prime_factors(number):
    list_of_primes = []
    for index in range(2,math.ceil(math.sqrt(number))+1):
        if is_prime(index) and number % index == 0 and number != index:
            list_of_primes.append(index)
    return list_of_primes